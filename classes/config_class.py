from datetime import datetime 
import os
class ProjectModelResnetConfig():
    model_name = "resnet"
    # Option for model depth [10, 18, 34, 50, 101, 152, 200]
    model_depth = 10
    input_W = 232
    input_H = 232
    input_D = 128
    no_cuda = True
    max_epoch = 50
    batch_size = 1
    resnet_shortcut = 'B'
    n_seg_classes = 4
    num_workers = 1
    pretrain_path = None
    phase_is_train = True
    pin_memory = None
    model_save_path = "./training_checkpoints/"
    model_save_filename = "Model_{}_{}_epoch{}_{}.pth.tar"
    
    @staticmethod
    def save_checkpoint_pathname(epoch:int) -> str:
        # datetime_str = datetime.now().strftime("%Y%m%d%H%M%S")
        datetime_str = ''
        filename = ProjectModelResnetConfig.model_save_filename.format(ProjectModelResnetConfig.model_name, ProjectModelResnetConfig.model_depth, epoch, datetime_str)
        return os.path.join(ProjectModelResnetConfig.model_save_path, filename)
        