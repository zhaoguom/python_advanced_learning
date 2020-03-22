from multiprocessing import Manager, Process

def add_data(p_dict, key, value):
    p_dict[key] = value


if __name__ == "__main__":
    progress_dict = Manager().dict()
    first_process = Process(target=add_data, args=(progress_dict, "zhaoguom1", 23))
    second_process = Process(target=add_data, args=(progress_dict, "zhaoguom2", 33))

    first_process.start()
    second_process.start()
    first_process.join()
    second_process.join()

    print(progress_dict)