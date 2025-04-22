from Task2 import classes_task2


def menu_task2():
    """
        Developer Pavel Zdor
        date: 20.04.2025
        menu function of task 2
        """
    txt = ""
    with open("C:/Users/pavel/PycharmProjects/Lab2/Task2_input.txt", "r", encoding='utf-8') as file:
        txt = file.read()
    data_worker = classes_task2.DataWorker(txt)
    data_worker.analyze_text()
    output_content = data_worker.analyze_text()
    classes_task2.write_file("C:/Users/pavel/PycharmProjects/Lab2/Task2_output.txt", output_content)

    with open("C:/Users/pavel/PycharmProjects/Lab2/Task2_output.txt", "r") as file:
        file_content = file.read()
        print(file_content)

    classes_task2.create_zip_archive("Task2_result.zip", "../Task2_output.txt")
