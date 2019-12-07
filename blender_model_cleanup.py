import bpy
import os
import glob

#24 armors/color steps
mmColor = {
    '5': (0.09758734714186246, 0.0015176349177441874, 0.14412847085805777, 1),
    '10': (0.06124605423161761, 0.001821161901293025, 0.1589608350608804, 1),
    '15': (0.03189603307301153, 0.001821161901293025, 0.17464740365558504, 1),
    '20': (0.010960094006488246, 0.001821161901293025, 0.1946178304415758, 1),
    '25': (0.0015176349177441874, 0.0024282158683907, 0.21223075741405523, 1),
    '30': (0.0015176349177441874, 0.016807375752887384, 0.23074004852434915, 1),
    '35': (0.0015176349177441874, 0.05126945837404324, 0.25415209433082675, 1),
    '40': (0.0015176349177441874, 0.11443537382697373, 0.27467731206038465, 1),
    '45': (0.0015176349177441874, 0.2195261997292692, 0.2961382707983211, 1),
    '50': (0.0015176349177441874, 0.32314320911295075, 0.27467731206038465, 1),
    '55': (0.0015176349177441874, 0.3467040563550296, 0.1714411007328226, 1),
    '60': (0.00121410793419535, 0.3712376804741491, 0.09084171118340768, 1),
    '65': (0.00121410793419535, 0.4019777798321958, 0.03560131487502034, 1),
    '70': (0.00121410793419535, 0.4286904966139066, 0.006512090792594475, 1),
    '75': (0.010329823029626936, 0.45641102318040466, 0.00121410793419535, 1),
    '80': (0.05126945837404324, 0.4910208498478356, 0.0009105809506465125, 1),
    '90': (0.14126329114027164, 0.5209955732043543, 0.0009105809506465125, 1),
    '95': (0.3005437944157765, 0.5520114015120001, 0.000607053967097675, 1),
    '100': (0.5457244613701866, 0.5906188409193369, 0.000607053967097675, 1),
    '110': (0.6239603916750761, 0.4072402119017367, 0.000607053967097675, 1),
    '120': (0.6583748172794485, 0.22696587351009836, 0.0003035269835488375, 1),
    '140': (0.7011018919329731, 0.09758734714186246, 0.0003035269835488375, 1),
    '145': (0.7379104087727308, 0.024157632448504756, 0.0, 1),
    '150': (0.7835377915261935, 0.0, 0.0009105809506465125, 1)
}

d = "C:\\Users\\dasu\\Desktop\\toclean\\"
sd = "C:\\Users\\dasu\\Desktop\\cleaned\\"
os.chdir(d)

for f in glob.glob("*.glb"):
    #cleanup previous scene
    s = bpy.context.scene        
    for o in s.objects:
        o.select_set(state=True)
    bpy.ops.object.delete()
    for block in bpy.data.meshes:
        if block.users == 0:
            bpy.data.meshes.remove(block)
    for block in bpy.data.materials:
        if block.users == 0:
            bpy.data.materials.remove(block)
    for block in bpy.data.textures:
        if block.users == 0:
            bpy.data.textures.remove(block)
    for block in bpy.data.images:
        if block.users == 0:
            bpy.data.images.remove(block)
    
    #import glb
    bpy.ops.import_scene.gltf(filepath=f,import_shading='FLAT')
    
    s = bpy.context.scene
    #remove autosmooth :vomit:
    for o in s.objects:
        if o.type == 'MESH':
            o.data.use_auto_smooth = False
            #fix armour naming
            for m in o.material_slots:
                if '.0' in m.name:
                    m.material = bpy.data.materials[m.material.name.split('.')[0]]

        #set colours to armour and internal components materials...all 26 of them...
        for m in bpy.data.materials:
        #internal components
            if m.name == 'M_SystemDebug_YELLOW':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (1,1,0,1)
                m.diffuse_color = (1,1,0,1)
                m.name = 'Turret Ring'
            elif m.name == 'M_SystemDebug_BLUE':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.300544,0.300544,0.89627,1)
                m.diffuse_color = (0.300544,0.300544,0.89627,1)
                m.name = 'Crew'
            elif m.name == 'M_SystemDebug' or m.name == 'M_SystemDebug_Inst':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.3,0.9,0.3,1)
                m.diffuse_color = (0.3,0.9,0.3,1)
                m.name = 'Tracks'
            elif m.name == 'M_SystemDebug_RED':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.89627,0.0802197,0.0802199,1)
                m.diffuse_color = (0.89627,0.0802197,0.0802199,1)
                m.name = 'Ammo Rack'
            elif m.name == 'M_SystemDebug_PURPLE':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (1,0.0998986,0.879623,1)
                m.diffuse_color = (1,0.0998986,0.879623,1)
                m.name = 'Engine'
            #armour MM
            elif m.name == 'MI_PS_Armor_5':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['5']
                m.diffuse_color = mmColor['5']
            elif m.name == 'MI_PS_Armor_10':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['10']
                m.diffuse_color = mmColor['10']
            elif m.name == 'MI_PS_Armor_15':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['15']
                m.diffuse_color = mmColor['15']
            elif m.name == 'MI_PS_Armor_20':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['20']
                m.diffuse_color = mmColor['20']
            elif m.name == 'MI_PS_Armor_25':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['25']
                m.diffuse_color = mmColor['25']
            elif m.name == 'MI_PS_Armor_30':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['30']
                m.diffuse_color = mmColor['30']
            elif m.name == 'MI_PS_Armor_35':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['35']
                m.diffuse_color = mmColor['35']
            elif m.name == 'MI_PS_Armor_40':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['40']
                m.diffuse_color = mmColor['40']
            elif m.name == 'MI_PS_Armor_45':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['45']
                m.diffuse_color = mmColor['45']
            elif m.name == 'MI_PS_Armor_50':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['50']
                m.diffuse_color = mmColor['50']
            elif m.name == 'MI_PS_Armor_55':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['55']
                m.diffuse_color = mmColor['55']
            elif m.name == 'MI_PS_Armor_60':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['60']
                m.diffuse_color = mmColor['60']
            elif m.name == 'MI_PS_Armor_65':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['65']
                m.diffuse_color = mmColor['65']
            elif m.name == 'MI_PS_Armor_70':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['70']
                m.diffuse_color = mmColor['70']
            elif m.name == 'MI_PS_Armor_75':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['75']
                m.diffuse_color = mmColor['75']
            elif m.name == 'MI_PS_Armor_80':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['80']
                m.diffuse_color = mmColor['80']
            elif m.name == 'MI_PS_Armor_90':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['90']
                m.diffuse_color = mmColor['90']
            elif m.name == 'MI_PS_Armor_95':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['95']
                m.diffuse_color = mmColor['95']
            elif m.name == 'MI_PS_Armor_100':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['100']
                m.diffuse_color = mmColor['100']
            elif m.name == 'MI_PS_Armor_110':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['110']
                m.diffuse_color = mmColor['110']
            elif m.name == 'MI_PS_Armor_120':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['120']
                m.diffuse_color = mmColor['120']
            elif m.name == 'MI_PS_Armor_140':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['140']
                m.diffuse_color = mmColor['140']
            elif m.name == 'MI_PS_Armor_145':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['145']
                m.diffuse_color = mmColor['145']
            elif m.name == 'MI_PS_Armor_150':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = mmColor['150']
                m.diffuse_color = mmColor['150']

        #clear customdata normals (idk if this is even needed :|)
        s = bpy.context.scene        
        for o in s.objects:
            o.select_set(state=True)
        selection = bpy.context.selected_objects
        for o in selection:
            if 'Node' in o.name:
                continue
            bpy.context.view_layer.objects.active = o
            bpy.ops.mesh.customdata_custom_splitnormals_clear()
        
        
        
        #export to cleaned folder
        bpy.ops.export_scene.gltf(export_format='GLB', check_existing=False, export_texcoords=False, 
                                  export_normals=False, export_materials=True, export_colors=False,
                                  export_animations=False, export_frame_range=False, export_skins=False,
                                  export_morph=False, export_all_influences=False, filepath=sd+f)
