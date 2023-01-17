# 2 Задание разработать программное обеспечение, где проводиться прогнозирование роста пшеницы, относительно различных факторов.
#  Показать нормализацию данных, матрицу векторов входных данных, выбрать несколько слоев, показать результат обучения


# импортируем библиотеки
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import pandas as pd

# нейронка в отдельном файле
from neuron import predict




# Root window
root = tk.Tk()
root.title('Задание 2')
root.geometry('810x400')

# создаем главный лейбл
main_label = ttk.Label(root, text="Выберите csv-файл(он должен состоять только из чисел) и нажмите кнопку 'Calculate'")
main_label.grid(column=0, row=0, sticky='w', padx=10, pady=10)

# Text editor
text = tk.Text(root, height=10, width=100)
text.grid(column=0, row=1, sticky='nsew', )



# Кнопка открытия файла
def open_text_file():
    global main_label
    # file type
    filetypes = (
        ('csv files', '*.csv*'),
        ('All files', '*.*')
    )
    # читаем датафрейм и передаем его в функцию predict
    file = fd.askopenfile(filetypes=filetypes)
    main_label.destroy()
    main_label = ttk.Label(root, text="Идет открытие файла...")
    main_label.grid(column=0, row=0, sticky='w', padx=10, pady=10)
    text.insert('1.0', pd.read_csv(file))
    return file.name

    
# функция расчета
def calculate():
    # немного глобалов, чтобы меньше париться
    global main_label, predict_label

    # удаляем старый текст
    main_label.destroy()
    main_label = ttk.Label(root, text="Идет расчет...")
    main_label.grid(column=0, row=0, sticky='w', padx=10, pady=10)
    # читаем файл
    data = pd.read_csv(open_text_file())
    
    # передаем данные нейронке
    predict(data)

    # делаем окно больше
    root.geometry('810x800')

    # получаем назад кортеж с результатами
    result = predict(data)
    print(result)

    # выводим результаты
    desc1_label = ttk.Label(root, text="confusion_matrix:")
    desc1_label.grid(column=0, row=3, sticky='w', padx=10, pady=10)

    predict_label2 = ttk.Label(root, text=result[1])
    predict_label2.grid(column=0, row=3, padx=10, pady=10)

    desc2_label = ttk.Label(root, text="accuracy_score:")
    desc2_label.grid(column=0, row=4, sticky='w', padx=10, pady=10)

    predict_label.destroy()
    predict_label = ttk.Label(root, text=result[0][:21])
    predict_label.grid(column=0, row=4, padx=10, pady=10)

    desc3_label = ttk.Label(root, text="Normalization:")
    desc3_label.grid(column=0, row=5, sticky='w', padx=10, pady=10)

    predict_label3 = ttk.Label(root, text="optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'], epochs = 100, batch_size = 10")
    predict_label3.grid(column=0, row=5, padx=10, pady=10)



    main_label.destroy()
    main_label = ttk.Label(root, text="Успешно!")
    main_label.grid(column=0, row=0, sticky='w', padx=10, pady=10)




# open file button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=open_text_file
)

# calculate button
open_button.grid(column=0, row=2, sticky='w', padx=10, pady=10)
calculate_button = ttk.Button(
    root,
    text='Calculate',
    command=calculate
)
calculate_button.grid(column=0, row=2, sticky='e', padx=10, pady=10)

# predict label
predict_label = ttk.Label(root, text="Тут появится результат")
predict_label.grid(column=0, row=3, sticky='w', padx=10, pady=10)

# скроллбар на деплое перестал работать без причины
scrollbar = ttk.Scrollbar(
    root,
    orient='vertical',
)
scrollbar.grid(column=1, row=1, sticky='nsew')


root.mainloop()

