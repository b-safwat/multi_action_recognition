import constants
import motion_cnn
import spatial_cnn
from average_fusion import fusion_accuracry
import os

#
# spatial_cnn.main(ds_path='/home/bassel/data/office-actions/office_actions_19/short_clips/stabilized_resized_frms_224/',
#      trainfile='/home/bassel/data/office-actions/office_actions_19/short_clips/labels/side_only_trainlist.txt',
#      testfile='/home/bassel/data/office-actions/office_actions_19/short_clips/labels/side_only_testlist.txt',
#      prefix="stabilized_side_view")
perspectives = ["side_only_testlist.txt", "front_only_testlist.txt", "testlist.txt"]  #
perspectives_names = ["side", "front", "all"]
perspectives = ["testlist.txt"]  #
perspectives_names = ["all"]

for step in [1, 2, 3, 4, 6]:
    import motion_cnn

    frame_count_filepath = "dataloader/dic/motion_frame_count.pickle"

    for i, perspective in enumerate(perspectives):
        print ("model trained at step: ", i+1)
        if os.path.isfile(frame_count_filepath):
            os.remove(frame_count_filepath)

        motion_cnn.main("/home/bassel/data/office-actions/office_actions_19/short_clips/flow_224/",
                        trainfile='/home/bassel/data/office-actions/office_actions_19/short_clips/labels/{}'.format(
                            perspective),
                        testfile='/home/bassel/data/office-actions/office_actions_19/short_clips/labels/{}'.format(
                            perspective),
                        prefix="step_{}_{}_view".format(step, perspectives_names[i]),
                        method=constants.EXPERIMENTS.MULTIPLE_STEPS__CLIPS_START_STEP_END,
                        evaluate=True,
                        resume_file="record/motion/step_{}_{}_view_checkpoint.pth.tar".format(step, perspectives_names[i]),
                        step=step)

# rgb_preds = 'record/spatial/stabilized_side_view_spatial_video_preds.pickle'
# opf_preds = 'record/motion/stabilized_side_view_motion_video_preds.pickle'
# ds_path = '/home/bassel/data/office-actions/office_actions_19/short_clips/stabilized_resized_frms_224'
# trainfile = '/home/bassel/data/office-actions/office_actions_19/short_clips/labels/side_only_trainlist.txt'
# testfile = '/home/bassel/data/office-actions/office_actions_19/short_clips/labels/side_only_testlist.txt'

# fusion_accuracry(rgb_preds, opf_preds, ds_path, trainfile, testfile)
