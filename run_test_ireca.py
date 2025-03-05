import os
os.environ["KERAS_BACKEND"] = "tensorflow"
os.environ["CUDA_VISIBLE_DEVICES"] = "1"  # 指定使用哪块GPU

from HyperParameters import *

if learning_rate_reward_shaping == 4e-6:
    for index_run in range(0,1):
        print('------------------> index run:', index_run)
        if bc_model_path_test == "./bc_runs_ireca/reproduce_test/cramped_room":
            print(f'bc_model_path_test: {bc_model_path_test}')
            with open('test_ireca.py', 'r', encoding='utf-8') as file:
                exec(file.read())
            # ----------------------
            np.save(f'./data/test/cr_ireca/rc_test_data_fading_ireca_return_shaped_{index_run}.npy', avg_return_shaped)
            np.save(f'./data/test/cr_ireca/rc_test_data_fading_ireca_return_sparse_{index_run}.npy', avg_return_sparse)
            np.save(f'./data/test/cr_ireca/rc_test_data_fading_ireca_return_cau_{index_run}.npy',    avg_return_cau)
            np.save(f'./data/test/cr_ireca/rc_test_data_fading_ireca_return_ent_{index_run}.npy',    avg_return_ent)
            np.save(f'./data/test/cr_ireca/rc_test_data_fading_ireca_return_env_{index_run}.npy',    avg_return_env)
            np.save(f'./data/test/cr_ireca/rc_test_data_fading_ireca_return_ireca_{index_run}.npy',   avg_return_ireca)
            np.save(f'./data/test/cr_ireca/rc_test_data_fading_ireca_softmax_env_{index_run}.npy',   coeff_reward_softmax_env)
            np.save(f'./data/test/cr_ireca/rc_test_data_fading_ireca_softmax_cau_{index_run}.npy',   coeff_reward_softmax_cau)
            np.save(f'./data/test/cr_ireca/rc_test_data_fading_ireca_softmax_ent_{index_run}.npy',   coeff_reward_softmax_ent)
#             ------------------
        elif bc_model_path_test == "./bc_runs_ireca/reproduce_test/asymmetric_advantages":
            print(f'bc_model_path: {bc_model_path_test}')
            with open('test_ireca.py', 'r', encoding='utf-8') as file:
                exec(file.read())
            # ----------------------
            np.save(f'./data/test/aa_ireca/aa_test_data_fading_ireca_return_shaped_{index_run}.npy', avg_return_shaped)
            np.save(f'./data/test/aa_ireca/aa_test_data_fading_ireca_return_sparse_{index_run}.npy', avg_return_sparse)
            np.save(f'./data/test/aa_ireca/aa_test_data_fading_ireca_return_cau_{index_run}.npy',    avg_return_cau)
            np.save(f'./data/test/aa_ireca/aa_test_data_fading_ireca_return_ent_{index_run}.npy',    avg_return_ent)
            np.save(f'./data/test/aa_ireca/aa_test_data_fading_ireca_return_env_{index_run}.npy',    avg_return_env)
            np.save(f'./data/test/aa_ireca/aa_test_data_fading_ireca_return_ireca_{index_run}.npy',   avg_return_ireca)
            np.save(f'./data/test/aa_ireca/aa_test_data_fading_ireca_softmax_env_{index_run}.npy',   coeff_reward_softmax_env)
            np.save(f'./data/test/aa_ireca/aa_test_data_fading_ireca_softmax_cau_{index_run}.npy',   coeff_reward_softmax_cau)
            np.save(f'./data/test/aa_ireca/aa_test_data_fading_ireca_softmax_ent_{index_run}.npy',   coeff_reward_softmax_ent)
