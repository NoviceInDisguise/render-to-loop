import bpy

scn = bpy.context.scene                 #set convenient variable to current scene
sel = bpy.context.selected_sequences    #set convenient variable to selected sequences

if len(sel) == 1:                           #if only one (1) sequence is selected, then execute

    track = sel[0]                          #set track to the element in the array
    str_len = track.frame_final_duration    #set variable to the length of selected sequence

    bpy.ops.sequencer.cut(frame=(str_len/2)+1,type='HARD',side='RIGHT') #cut track in half

    #update selected
    sel = bpy.context.selected_sequences    #reset sel to selected sequences
    track = sel[0]                          #reset track to the element in the array

    #move track
    track.channel = track.channel+1     #move right sequence up one channel
    track.frame_start = 1               #move sequence to frame 1

    ############################
    #keyframe top track opacity#
    ############################
    path = bpy.context.selected_sequences         #get data path
    data_str = str(path)                          #convert data path to string
    data_str = data_str.split("scenes['Scene'].") #split string in to a list
    data_str = data_str[-1]                       #get last piece
    data_str = data_str[:-1]                      #remove last character
    print("Selected sequence data path: " + str(data_str))

    #set to 1
    track.blend_alpha = 1                                                   #set alpha blend value
    scn.keyframe_insert(data_path=data_str + ".blend_alpha",frame=float(1)) #keyframe alpha blend value
    print("Keyframe set on frame 1.0")

    #set to 0
    track.blend_alpha = 0                                                           #set alpha blend value
    scn.keyframe_insert(data_path=data_str + ".blend_alpha",frame=float(str_len/2)) #keyframe alpha blend value
    print("Keyframe set on frame " + str(str_len/2))

    scn.frame_end = str_len/2                   #set end frame to last frame
    print("End frame set to " + str(str_len/2)) #print strip length

elif len(sel_sequence) > 1: 
    print("ERROR: Multiple sequences selected")

elif len(sel_sequence) < 1: 
    print("ERROR: Please select a valid sequence")

else: print("ERROR: Unknown error")
