import os.path as osp


ROOT_DIR = osp.dirname(osp.abspath(__file__))
LOCAL_LOG_DIR = osp.join(ROOT_DIR, 'data')

train_cfg = {
        # general
        'seed': 0,
        'iteration_num': 1e3,
        'task_sample_num': 32,
        'task_sample_frequency': 10,
        'traj_sample_num': 100,
        'eval_frequency': 10,
        'eval_sample_num': 1,
        # adaptation
        'adaptation_update_num': 5,
        # learning rate
        'phi': 1e-4,
        'beta': 1e-3,
        'eta': 3e-4,
        # sample
        'M': 16,
        'K': 16,
        'rollout_len': 32, # >= M+K
        'rollout_num': 16,
        # dataset
        'dataset_size': 1e3,
        # loss
        'loss_type': 'mse',
        'loss_scale': 100,
        }

test_cfg = {
        'seed': 0,
        'iteration_num': 2e3,
        }

net_cfg = {
        'hid_shape': 32,
        'hid_num': 2,
        'activation': 'tanh',
        }

controller_cfg = {
        'K': 1000, # sample num
        'T': 15, # horizon
        'lamda': 1.0,
        }
