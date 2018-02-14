import csv
import os
import time

while True:
    print("-" * 80)
    print("MIND LAB CONDITIONS FILE TEMPLATE CREATOR.")
    print("-" * 80)

    print("""In order to create properly format the files, please answer a
few questions about the experiment.""")

    print("How many participants do you need to make conditions files for?: ")
    participant_number = int(input(">"))

    print("How many sessions were there in the experiment?: ")
    total_sessions = int(input(">"))

    print("How many sensors were used on each participant?: ")
    cond_per_participant = int(input(">"))

    while True:
        proper_sensors = ["FNIRS", "EDA", "ECG",
                          "EEG", "RESP", "GSR",
                          "EYET"]
        print("Please enter the sensor types separated by a space:")
        sensor_list = input(">")
        sensor_list = sensor_list.split(" ")
        sensor_list = [s.upper() for s in sensor_list]
        not_proper = [s for s in sensor_list if s not in proper_sensors]
        if not not_proper and len(sensor_list) == cond_per_participant:
            break
        print("-" * 80)
        print("That is not proper input. Please try again.")
        print(f"Acceptable values: {proper_sensors}")
        print("-" * 80)

    while True:
        print("Please enter the experient ID number: ")
        experiment_id = input(">")
        if len(experiment_id) == 2 and experiment_id.isnumeric():
            break
        print("-" * 80)
        print("That is not proper input. Please try again.")
        print(f"Acceptable values must be a two digit interger.")
        print("-" * 80)

    task_num_per_session = []
    for i, session in enumerate(range(0, total_sessions)):
        while True:
            if total_sessions == 1:
                print("How many tasks were in the experiment?")
            else:
                print(f"How many tasks were in session {i + 1}?: ")
            try:
                task_num = int(input(">"))
            except ValueError as e:
                print(e)
                print("Please enter an interger.")
            if task_num > 0:
                task_num = int(task_num)
                task_num_per_session.append(task_num)
                break
            else:
                print("Task Number must be an interger greater than zero.")


    total_files = participant_number * cond_per_participant * total_sessions

    if not os.path.exists(f"{os.getcwd()}/exports/"):
        os.mkdir(f"{os.getcwd()}/exports/")

    os.chdir(f"{os.getcwd()}/exports/")

    fnames = []
    for i_session, session in enumerate(range(0, total_sessions)):
        for i_cond, cond in enumerate(range(0, cond_per_participant)):
            for i, fname in enumerate(range(0, participant_number)):
                i = i + 1
                str_i = str(i)
                if len(str_i) < 2:
                    str_i = f"0{str_i}"
                fname = f"{experiment_id}{str_i}_{sensor_list[i_cond]}_conditions_s{i_session + 1}.csv"
                print(fname)
                fnames.append(fname)

    print("Above are the file names that will be generated by this script.")
    for i, task_num in enumerate(task_num_per_session):
        print(f"Session {i + 1} has {task_num} tasks.")
    print("Do the above appear to be correct?: ")
    ans = input("(Y/n)")
    if ans[0].upper() == "Y":
        break
    print("Okay, lets try again then.")
    time.sleep(2)
    os.system("clear")

# while True:
#     print("Input a directory name for your files to go in (letters, and '_'s only): ")
#     user_dir = input(">")
#
#     if os.path.exists(f"{os.getcwd()}/{user_dir}"):
#         print(f"Directory, '{os.getcwd()}/{user_dir}' already exists. Use? (Y/n)")
#         ans = input(">")
#         if ans[0].upper == "Y":
#             os.chdir(f"{user_dir}")
#         else:
#             print("Okay, enter a new name.")
#     elif user_dir.replace("_", "").isalpha():
#         os.mkdir(f"{os.getcwd()}/{user_dir}")
#         os.chdir(f"{user_dir}")
#         break
#     else:
#         print(f"{user_dir} is not a valid directory name. Try something else.")
#
#     if ans[0].upper() == "Y":
#         break

for fname in fnames:
    for i, task_num in enumerate(task_num_per_session):
        if int(fname[-5]) == i + 1:
            task_row = [f"Task{x + 1}" for x in range(0, task_num)]
            task_row.insert(0, "")
            onset_row = ["" for x in range(0, task_num)]
            onset_row.insert(0, "onset")
            duration_row = ["" for x in range(0, task_num)]
            duration_row.insert(0, "duration")
            stim_row = ["" for x in range(0, task_num)]
            stim_row.insert(0, "stim")
            tlxm_row = ["" for x in range(0, task_num)]
            tlxm_row.insert(0, "TLX_Mental")
            tlxph_row = ["" for x in range(0, task_num)]
            tlxph_row.insert(0, "TLX_Physical")
            tlxt_row = ["" for x in range(0, task_num)]
            tlxt_row.insert(0, "TLX_Temporal")
            tlxp_row = ["" for x in range(0, task_num)]
            tlxp_row.insert(0, "TLX_Performance")
            tlxe_row = ["" for x in range(0, task_num)]
            tlxe_row.insert(0, "TLX_Effort")
            tlxf_row = ["" for x in range(0, task_num)]
            tlxf_row.insert(0, "TLX_Frustration")
            print(fname)
            print(task_row)

            file_rows = [task_row, onset_row, duration_row,
                         stim_row, tlxm_row, tlxph_row,
                         tlxt_row, tlxp_row, tlxe_row, tlxf_row]

            with open(f"{fname}", "w") as out_csv:
                 writer = csv.writer(out_csv, delimiter=",")

                 for row in file_rows:
                     writer.writerow(row)