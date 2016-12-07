import bpy

#set convenient variable to current scene
scn = bpy.context.scene

#check selected sequences
sel_sequence = bpy.context.selected_sequences

if len(sel_sequence) == 1:
    
    track = sel_sequence[0]
    
    #get length of strip
    str_len = track.frame_final_duration
    
    #cut track in half
    scn.frame_current = str_len/2
    bpy.ops.sequencer.cut(frame=(str_len/2),type='HARD',side='RIGHT')
    
    #update selected
    sel_sequence = bpy.context.selected_sequences
    track = sel_sequence[0]

    #move track
    track.channel = track.channel+1
    track.frame_start = 1

    ############################
    #keyframe top track opacity#
    ############################
    path = bpy.context.selected_sequences         #get data path
    data_str = str(path)                          #convert data path to string
    data_str = data_str.split("scenes['Scene'].") #split string in to a list
    data_str = data_str[-1]                       #get last piece
    data_str = data_str[:-1]                      #remove last character
    print(data_str)
    
    #set to 1
    track.blend_alpha = 1                                                   #set alpha blend value
    scn.keyframe_insert(data_path=data_str + ".blend_alpha",frame=float(1)) #keyframe alpha blend value
    #print("Keyframe set on frame 1")

    #set to 0
    track.blend_alpha = 0                                                           #set alpha blend value
    scn.keyframe_insert(data_path=data_str + ".blend_alpha",frame=float(str_len/2)) #keyframe alpha blend value
    #print("Keyframe set on frame " + str(str_len/2))

    scn.frame_end = str_len/2       #set end frame to last frame

    print(str_len)                  #print strip length

elif len(sel_sequence) > 1: 
    print("ERROR: Multiple sequences selected")

elif len(sel_sequence) < 1: 
    print("ERROR: Please select a valid sequence")

else: print("ERROR: Unknown error")
