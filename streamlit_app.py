import os
import tempfile
import sys
from io import StringIO

import streamlit as st
from cad_to_shapely import dxf, utils

from sectionproperties.pre.geometry import Geometry
from sectionproperties.analysis.section import Section

import matplotlib.pyplot as plt


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

    #if option == 'useful':
    st.code(code)
    #else: #raw
    #    st.code(code)

    #st.download_button(
    #    label="Download as smath file",
    #    data=code,
    #    file_name='.sm',
    #    mime='text/xml',
    #)    

    os.unlink(tmp_file.name)





