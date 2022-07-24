import os

import tempfile
import sys
from io import StringIO, BytesIO
import base64

import streamlit as st
from cad_to_shapely import dxf, utils

from sectionproperties.pre.geometry import Geometry
from sectionproperties.analysis.section import Section

import matplotlib.pyplot as plt
import template

uploaded_file = st.file_uploader(
    label = "Upload a CAD section file",
    type = ['dxf']
)


if uploaded_file is not None:
    tmp_file = tempfile.NamedTemporaryFile(delete=False)
    tmp_file.write(uploaded_file.getvalue())
    tmp_file.close() 
    my_dxf = dxf.DxfImporter(tmp_file.name)

    my_dxf.process(spline_delta = 0.1)   
    my_dxf.polygonize(
        force_zip = False
    )
    
    polygons = my_dxf.polygons

    fig, ax = plt.subplots()

    new = utils.find_holes(polygons)

    geom = Geometry(new)
    geom.create_mesh([1])
    section = Section(geom)

    section.plot_mesh(alpha=0.1, ax = ax, render = False)

    x,y = new.exterior.xy
    ax.plot(x,y)
    for hole in new.interiors:
        x,y = hole.xy
        ax.plot(x,y)

    with st.spinner('Talk amongst yourselves. I may be some time...'):
        section.calculate_geometric_properties()
        section.calculate_plastic_properties()
        section.plot_centroids(ax = ax, render = False)

    section.plot_centroids(ax = ax, render = False)
    ax.set_aspect('equal')


    buf = BytesIO()
    plt.savefig(buf,format='png')
    buf.seek(0)
    encoded_png =base64.b64encode(buf.getvalue()).decode()

    st.pyplot(fig)

    original_stdout = sys.stdout # Save a reference to the original standard output
    sys.stdout = string_io = StringIO()
    section.display_results(fmt = '.2f')
    sys.stdout = original_stdout

    code = string_io.getvalue()
    string_io.close()

    #option = st.selectbox(
    # 'How do you wnat section properties formatted?',
    # ('pretty', 'Raw'))

    local_is_principal = False
    angle = section.get_phi()
    if abs(angle)<0.01 or abs(angle-90)<0.01:
        local_is_principal = True


    with st.expander("sMath reporting"):
        image = st.checkbox('include image of section', value = True)

        if not local_is_principal:
            st.write(f'Local and principal badning axes are different (θ= {angle:.1f}°)')
            local = st.checkbox('include local axis properties', value = True)
            principal = st.checkbox('included principal axis properties', value = True)

        plastic = st.checkbox('include plastic properties', value = True)
        verbose = st.checkbox('include EVERYTHING', value = False)


        xml = template.smath_xml(
            a = section.get_area(),
            p = section.get_perimeter(),
            c = section.get_c(),
            ic = section.get_ic(),
            z = section.get_z(),
            s = section.get_s(),
            rc = section.get_rc(),
            ip = section.get_ip(),
            zp = section.get_zp(),
            sp = section.get_sp(),
            rp = section.get_rp(),        
            encoded_png =encoded_png
        )

        st.download_button(
            label="Download as smath file",
            data=xml,
            file_name='section.sm',
            mime='text/xml',
        )  

    st.code(code)


  

    os.unlink(tmp_file.name) #remove temp file


