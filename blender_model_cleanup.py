import bpy
import os
import glob

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
            elif m.name == 'MI_PS_Armor_10':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.006048833022857054, 0.13286832155381798, 0.7605245046752924, 1)
                m.diffuse_color = (0.006048833022857054, 0.13286832155381798, 0.7605245046752924, 1)
            elif m.name == 'MI_PS_Armor_15':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.006048833022857054, 0.32314320911295075, 0.7605245046752924, 1)
                m.diffuse_color = (0.006048833022857054, 0.32314320911295075, 0.7605245046752924, 1)
            elif m.name == 'MI_PS_Armor_20':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.006512090792594475, 0.6239603916750761, 0.768151147247507, 1)
                m.diffuse_color = (0.006512090792594475, 0.6239603916750761, 0.768151147247507, 1)
            elif m.name == 'MI_PS_Armor_25':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.006512090792594475, 0.7758222183174236, 0.5520114015120001, 1)
                m.diffuse_color = (0.006512090792594475, 0.7758222183174236, 0.5520114015120001, 1)
            elif m.name == 'MI_PS_Armor_30':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.006995410187265387, 0.7758222183174236, 0.2788942634768104, 1)
                m.diffuse_color = (0.006995410187265387, 0.7758222183174236, 0.2788942634768104, 1)
            elif m.name == 'MI_PS_Armor_40':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.006995410187265387, 0.7835377915261935, 0.10702310297826761, 1)
                m.diffuse_color = (0.006995410187265387, 0.7835377915261935, 0.10702310297826761, 1)
            elif m.name == 'MI_PS_Armor_45':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.007499032043226175, 0.7912979403326302, 0.02217388479338738, 1)
                m.diffuse_color = (0.007499032043226175, 0.7912979403326302, 0.02217388479338738, 1)
            elif m.name == 'MI_PS_Armor_50':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.03560131487502034, 0.7912979403326302, 0.007499032043226175, 1)
                m.diffuse_color = (0.03560131487502034, 0.7912979403326302, 0.007499032043226175, 1)
            elif m.name == 'MI_PS_Armor_55':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.14412847085805777, 0.799102738014409, 0.008023192985384994, 1)
                m.diffuse_color = (0.14412847085805777, 0.799102738014409, 0.008023192985384994, 1)
            elif m.name == 'MI_PS_Armor_60':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.3467040563550296, 0.8069522576692516, 0.008023192985384994, 1)
                m.diffuse_color = (0.3467040563550296, 0.8069522576692516, 0.008023192985384994, 1)
            elif m.name == 'MI_PS_Armor_65':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.6583748172794485, 0.8148465722161012, 0.008568125618069307, 1)
                m.diffuse_color = (0.6583748172794485, 0.8148465722161012, 0.008568125618069307, 1)
            elif m.name == 'MI_PS_Armor_70':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8148465722161012, 0.5840784178911641, 0.008568125618069307, 1)
                m.diffuse_color = (0.8148465722161012, 0.5840784178911641, 0.008568125618069307, 1)
            elif m.name == 'MI_PS_Armor_75':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8227857543962835, 0.3005437944157765, 0.009134058702220787, 1)
                m.diffuse_color = (0.8227857543962835, 0.3005437944157765, 0.009134058702220787, 1)
            elif m.name == 'MI_PS_Armor_80':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8307698767746546, 0.11953842798834562, 0.00972121732023785, 1)
                m.diffuse_color = (0.8307698767746546, 0.11953842798834562, 0.00972121732023785, 1)
            elif m.name == 'MI_PS_Armor_90':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8307698767746546, 0.026241221894849898, 0.00972121732023785, 1)
                m.diffuse_color = (0.8307698767746546, 0.026241221894849898, 0.00972121732023785, 1)
            elif m.name == 'MI_PS_Armor_95':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.83879901174074, 0.010329823029626936, 0.042311410620809675, 1)
                m.diffuse_color = (0.83879901174074, 0.010329823029626936, 0.042311410620809675, 1)
            elif m.name == 'MI_PS_Armor_100':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.846873231509858, 0.010329823029626936, 0.1589608350608804, 1)
                m.diffuse_color = (0.846873231509858, 0.010329823029626936, 0.1589608350608804, 1)
            elif m.name == 'MI_PS_Armor_120':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.846873231509858, 0.010960094006488246, 0.3712376804741491, 1)
                m.diffuse_color = (0.846873231509858, 0.010960094006488246, 0.3712376804741491, 1)
            elif m.name == 'MI_PS_Armor_140':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8549926081242338, 0.010960094006488246, 0.7011018919329731, 1)
                m.diffuse_color = (0.8549926081242338, 0.010960094006488246, 0.7011018919329731, 1)
            elif m.name == 'MI_PS_Armor_145':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.6239603916750761, 0.011612245179743885, 0.8631572134541023, 1)
                m.diffuse_color = (0.6239603916750761, 0.011612245179743885, 0.8631572134541023, 1)
            elif m.name == 'MI_PS_Armor_150':
                m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.32314320911295075, 0.012286488356915872, 0.8631572134541023, 1)
                m.diffuse_color = (0.32314320911295075, 0.012286488356915872, 0.8631572134541023, 1)

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
