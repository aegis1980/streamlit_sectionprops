def smath_xml(
    a,p,c,ic,z,s,rc,ip,zp,sp,rp,encoded_png : str
):

    return f"""
    <?xml version="1.0" encoding="utf-8" standalone="yes"?>
<?application progid="SMath Studio Desktop" version="0.99.7921.69"?>
<worksheet xmlns="http://smath.info/schemas/worksheet/1.0">
  <settings ppi="120">
    <identity>
      <id>ba008abc-f2c0-44c6-81a6-b7675c413e6d</id>
      <revision>15</revision>
    </identity>
    <calculation>
      <precision>4</precision>
      <exponentialThreshold>5</exponentialThreshold>
      <trailingZeros>false</trailingZeros>
      <significantDigitsMode>false</significantDigitsMode>
      <roundingMode>0</roundingMode>
      <fractions>decimal</fractions>
    </calculation>
    <pageModel active="false" viewMode="2" printGrid="false" printAreas="true" simpleEqualsOnly="false" printBackgroundImages="true">
      <paper id="1" orientation="Portrait" width="850" height="1100" />
      <margins left="39" right="39" top="49" bottom="49" />
      <header alignment="Center" color="#a9a9a9">&amp;[DATE] &amp;[TIME] - &amp;[FILENAME]</header>
      <footer alignment="Center" color="#a9a9a9">&amp;[PAGENUM] / &amp;[COUNT]</footer>
      <backgrounds />
    </pageModel>
    <dependencies>
      <assembly name="SMath Studio Desktop" version="0.99.7921.69" guid="a37cba83-b69c-4c71-9992-55ff666763bd" />
      <assembly name="MathRegion" version="1.11.7921.69" guid="02f1ab51-215b-466e-a74d-5d8b1cf85e8d" />
      <assembly name="PictureRegion" version="1.10.7921.69" guid="06b5df04-393e-4be7-9107-305196fcb861" />
      <assembly name="TextRegion" version="1.11.7921.69" guid="485d28c5-349a-48b6-93be-12a35a1c1e39" />
    </dependencies>
  </settings>
  <regions type="content">
    <region left="45" top="108" width="426" height="278" color="#000000">
      <picture>
       <raw format="png" encoding="base64">{encoded_png}</raw>
      </picture>
    </region>
    <region left="27" top="414" width="190" height="23" color="#000000" fontSize="10">
      <text lang="eng" fontFamily="Arial" fontSize="10">
        <content>
          <p style="font-weight: bold;">Basic geometric properties </p>
        </content>
      </text>
    </region>
    <region left="54" top="441" width="84" height="33" color="#000000" fontSize="10">
      <math>
        <description active="true" position="Right" lang="eng">
          <content>
            <p>Area</p>
          </content>
        </description>
        <input>
          <e type="operand">A</e>
          <e type="operand">{a}</e>
          <e type="operand" style="unit">mm</e>
          <e type="operand">2</e>
          <e type="operator" args="2">^</e>
          <e type="operator" args="2">*</e>
          <e type="operator" args="2">:</e>
        </input>
      </math>
    </region>
    <region left="54" top="477" width="74" height="24" color="#000000" fontSize="10">
      <math>
        <description active="true" position="Right" lang="eng">
          <content>
            <p>Perimeter</p>
          </content>
        </description>
        <input>
          <e type="operand">p</e>
          <e type="operand">{p}</e>
          <e type="operand" style="unit">mm</e>
          <e type="operator" args="2">*</e>
          <e type="operator" args="2">:</e>
        </input>
      </math>
    </region>
    <region left="54" top="504" width="95" height="27" color="#000000" fontSize="10">
      <math>
        <description active="true" position="Right" lang="eng">
          <content>
            <p>Centre of mass</p>
          </content>
        </description>
        <input>
          <e type="operand">c</e>
          <e type="operand">{c[0]}</e>
          <e type="operand">{c[1]}</e>
          <e type="operand">1</e>
          <e type="operand">2</e>
          <e type="function" args="4">mat</e>
          <e type="operand" style="unit">mm</e>
          <e type="operator" args="2">*</e>
          <e type="operator" args="2">:</e>
        </input>
      </math>
    </region>
    <region left="27" top="540" width="264" height="23" color="#000000" fontSize="10">
      <text lang="eng" fontFamily="Arial" fontSize="10">
        <content>
          <p style="font-weight: bold;">Properties about imported (xx,yy) axes </p>
        </content>
      </text>
    </region>
    <region left="54" top="567" width="113" height="39" color="#000000" fontSize="10">
      <math>
        <input>
          <e type="operand">I.xx</e>
          <e type="operand">{ic[0]}</e>
          <e type="operand" style="unit">mm</e>
          <e type="operand">4</e>
          <e type="operator" args="2">^</e>
          <e type="operator" args="2">*</e>
          <e type="operator" args="2">:</e>
        </input>
      </math>
    </region>
    <region left="189" top="567" width="113" height="39" color="#000000" fontSize="10">
      <math>
        <input>
          <e type="operand">I.yy</e>
          <e type="operand">{ic[1]}</e>
          <e type="operand" style="unit">mm</e>
          <e type="operand">4</e>
          <e type="operator" args="2">^</e>
          <e type="operator" args="2">*</e>
          <e type="operator" args="2">:</e>
        </input>
      </math>
    </region>
    <region left="306" top="567" width="113" height="39" color="#000000" fontSize="10">
      <math>
        <description active="true" position="Right" lang="eng">
          <content>
            <p>2nd moments of area, geometric axes</p>
          </content>
        </description>
        <input>
          <e type="operand">I.xy</e>
          <e type="operand">{ic[2]}</e>
          <e type="operand" style="unit">mm</e>
          <e type="operand">4</e>
          <e type="operator" args="2">^</e>
          <e type="operator" args="2">*</e>
          <e type="operator" args="2">:</e>
        </input>
      </math>
    </region>
    <region left="54" top="612" width="104" height="45" color="#000000" fontSize="10">
      <math>
        <input>
          <e type="operand">Z.xx</e>
          <e type="operand">{z[0]}</e>
          <e type="operand">{z[1]}</e>
          <e type="operand">2</e>
          <e type="operand">1</e>
          <e type="function" args="4">mat</e>
          <e type="operand" style="unit">mm</e>
          <e type="operand">3</e>
          <e type="operator" args="2">^</e>
          <e type="operator" args="2">*</e>
          <e type="operator" args="2">:</e>
        </input>
      </math>
    </region>
    <region left="162" top="612" width="104" height="45" color="#000000" fontSize="10">
      <math>
        <description active="true" position="Right" lang="eng">
          <content>
            <p>Elastic sections (top &amp; btm), geometric axes</p>
          </content>
        </description>
        <input>
          <e type="operand">Z.yy</e>
          <e type="operand">{z[2]}</e>
          <e type="operand">{z[3]}1</e>
          <e type="operand">2</e>
          <e type="operand">1</e>
          <e type="function" args="4">mat</e>
          <e type="operand" style="unit">mm</e>
          <e type="operand">3</e>
          <e type="operator" args="2">^</e>
          <e type="operator" args="2">*</e>
          <e type="operator" args="2">:</e>
        </input>
      </math>
    </region>
    <region left="54" top="657" width="89" height="39" color="#000000" fontSize="10">
      <math>
        <input>
          <e type="operand">S.xx</e>
          <e type="operand">{s[0]}</e>
          <e type="operand" style="unit">mm</e>
          <e type="operand">3</e>
          <e type="operator" args="2">^</e>
          <e type="operator" args="2">*</e>
          <e type="operator" args="2">:</e>
        </input>
      </math>
    </region>
    <region left="162" top="657" width="89" height="39" color="#000000" fontSize="10">
      <math>
        <description active="true" position="Right" lang="eng">
          <content>
            <p>Plastic sections, geometric axes</p>
          </content>
        </description>
        <input>
          <e type="operand">S.yy</e>
          <e type="operand">{s[1]}</e>
          <e type="operand" style="unit">mm</e>
          <e type="operand">3</e>
          <e type="operator" args="2">^</e>
          <e type="operator" args="2">*</e>
          <e type="operator" args="2">:</e>
        </input>
      </math>
    </region>
    <region left="54" top="720" width="87" height="30" color="#000000" fontSize="10">
      <math>
        <input>
          <e type="operand">r.xx</e>
          <e type="operand">{rc[0]}</e>
          <e type="operand" style="unit">mm</e>
          <e type="operator" args="2">*</e>
          <e type="operator" args="2">:</e>
        </input>
      </math>
    </region>
    <region left="171" top="720" width="87" height="30" color="#000000" fontSize="10">
      <math>
        <description active="true" position="Right" lang="eng">
          <content>
            <p>Radii of gyration, geometric axes</p>
          </content>
        </description>
        <input>
          <e type="operand">r.yy</e>
          <e type="operand">{rc[1]}</e>
          <e type="operand" style="unit">mm</e>
          <e type="operator" args="2">*</e>
          <e type="operator" args="2">:</e>
        </input>
      </math>
    </region>
    <region left="27" top="774" width="262" height="23" color="#000000" fontSize="10" isBreakable="false">
      <text lang="eng" fontFamily="Arial" fontSize="10">
        <content>
          <p style="font-weight: bold;">Properties about principal (11,22) axes </p>
        </content>
      </text>
    </region>
    <region left="54" top="801" width="113" height="39" color="#000000" fontSize="10">
      <math>
        <input>
          <e type="operand">I.11</e>
          <e type="operand">{ip[0]}</e>
          <e type="operand" style="unit">mm</e>
          <e type="operand">4</e>
          <e type="operator" args="2">^</e>
          <e type="operator" args="2">*</e>
          <e type="operator" args="2">:</e>
        </input>
      </math>
    </region>
    <region left="162" top="801" width="113" height="39" color="#000000" fontSize="10">
      <math>
        <input>
          <e type="operand">I.22</e>
          <e type="operand">{ip[1]}</e>
          <e type="operand" style="unit">mm</e>
          <e type="operand">4</e>
          <e type="operator" args="2">^</e>
          <e type="operator" args="2">*</e>
          <e type="operator" args="2">:</e>
        </input>
      </math>
    </region>
    <region left="54" top="846" width="104" height="45" color="#000000" fontSize="10">
      <math>
        <input>
          <e type="operand">Z.11</e>
          <e type="operand">{zp[0]}</e>
          <e type="operand">{zp[1]}</e>
          <e type="operand">2</e>
          <e type="operand">1</e>
          <e type="function" args="4">mat</e>
          <e type="operand" style="unit">mm</e>
          <e type="operand">3</e>
          <e type="operator" args="2">^</e>
          <e type="operator" args="2">*</e>
          <e type="operator" args="2">:</e>
        </input>
      </math>
    </region>
    <region left="162" top="846" width="104" height="45" color="#000000" fontSize="10">
      <math>
        <description active="true" position="Right" lang="eng">
          <content>
            <p>Elastic sections (top &amp; btm), principal axes</p>
          </content>
        </description>
        <input>
          <e type="operand">Z.22</e>
          <e type="operand">{zp[2]}</e>
          <e type="operand">{zp[3]}</e>
          <e type="operand">2</e>
          <e type="operand">1</e>
          <e type="function" args="4">mat</e>
          <e type="operand" style="unit">mm</e>
          <e type="operand">3</e>
          <e type="operator" args="2">^</e>
          <e type="operator" args="2">*</e>
          <e type="operator" args="2">:</e>
        </input>
      </math>
    </region>
    <region left="54" top="891" width="89" height="39" color="#000000" fontSize="10">
      <math>
        <input>
          <e type="operand">S.11</e>
          <e type="operand">{sp[0]}</e>
          <e type="operand" style="unit">mm</e>
          <e type="operand">3</e>
          <e type="operator" args="2">^</e>
          <e type="operator" args="2">*</e>
          <e type="operator" args="2">:</e>
        </input>
      </math>
    </region>
    <region left="162" top="891" width="89" height="39" color="#000000" fontSize="10">
      <math>
        <description active="true" position="Right" lang="eng">
          <content>
            <p>Plastic sections, principal axes</p>
          </content>
        </description>
        <input>
          <e type="operand">S.22</e>
          <e type="operand">{sp[1]}</e>
          <e type="operand" style="unit">mm</e>
          <e type="operand">3</e>
          <e type="operator" args="2">^</e>
          <e type="operator" args="2">*</e>
          <e type="operator" args="2">:</e>
        </input>
      </math>
    </region>
    <region left="54" top="945" width="87" height="30" color="#000000" fontSize="10">
      <math>
        <input>
          <e type="operand">r.11</e>
          <e type="operand">{rp[0]}</e>
          <e type="operand" style="unit">mm</e>
          <e type="operator" args="2">*</e>
          <e type="operator" args="2">:</e>
        </input>
      </math>
    </region>
    <region left="171" top="945" width="87" height="30" color="#000000" fontSize="10">
      <math>
        <description active="true" position="Right" lang="eng">
          <content>
            <p>Radii of gyration, principal axes</p>
          </content>
        </description>
        <input>
          <e type="operand">r.22</e>
          <e type="operand">{rp[1]}</e>
          <e type="operand" style="unit">mm</e>
          <e type="operator" args="2">*</e>
          <e type="operator" args="2">:</e>
        </input>
      </math>
    </region>
  </regions>
</worksheet>
    """