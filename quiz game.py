from tkinter import *

def start_main_page():
    def start_game(args):
        main_window.destroy()
        if args == 1:
            from Options import Animals
            Animals.main()
        elif args == 2:
            from Options import Body_parts
            Body_parts.main()
        elif args == 3:
            from Options import Colour
            Colour.main()
        elif args == 4:
            from Options import Fruit
            Fruit.main()
        elif args == 5:
            from Options import Shapes
            Shapes.main()
        elif args == 6:
            from Options import Vegetable
            Vegetable.main()
        elif args == 7:
            from Options import Vehicles
            Vehicles.main()

    def option():

        lab_img1 = Button(
            main_window,
            image=img1,
            bg='#e6fff5',
            border=0,
            justify='center',

        )
        sel_btn1 = Button(
            text="Animals",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(1),
        )

        sel_btn2 = Button(
            text="Body parts",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(2),
        )

        sel_btn3 = Button(
            text="Colour",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(3),
        )

        sel_btn4 = Button(
            text="Fruits",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(4),
        )

        sel_btn5 = Button(
            text="Shapes",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(5),
        )

        sel_btn6 = Button(
            text="Vegetable",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(6),
        )

        sel_btn7 = Button(
            text="Vehicles",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(7),
        )
        lab_img1.grid(row=0, column=0, padx=20)
        sel_btn1.grid(row=0, column=4, pady=(10, 0), padx=50, )
        sel_btn2.grid(row=1, column=4, pady=(10, 0), padx=50, )
        sel_btn3.grid(row=2, column=4, pady=(10, 0), padx=50, )
        sel_btn4.grid(row=3, column=4, pady=(10, 0), padx=50, )
        sel_btn5.grid(row=4, column=4, pady=(10, 0), padx=50, )
        sel_btn6.grid(row=5, column=4, pady=(10, 0), padx=50, )
        sel_btn7.grid(row=6, column=4, pady=(10, 0), padx=50, )

    def show_option():
        start_btn.destroy()

        lab_img.destroy()
        option()

    main_window = Tk()

    main_window.geometry("500x500+500+150")
    main_window.resizable(0, 0)
    main_window.title("IT SOURCECODE --->> Jumbled Words Quiz")
    main_window.configure(background="#e6fff5")

    img0 = PhotoImage(file="logo1.png")
    img1 = PhotoImage(file="back.png")

    lab_img = Label(
        main_window,
        image=img0,
        bg='#e6fff5',
    )
    lab_img.pack(pady=(50, 0))

    start_btn = Button(
        main_window,
        text="Start",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="green",
        font=("", 13),
        cursor="hand2",
        command=show_option,
    )
    start_btn.pack(pady=(50, 20))

    main_window.mainloop()


start_main_page()

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
from tkinter import *
 
def start_main_page():
    def start_game(args):
        main_window.destroy()
        if args == 1:
            from Options import Animals
            Animals.main()
        elif args == 2:
            from Options import Body_parts
            Body_parts.main()
        elif args == 3:
            from Options import Colour
            Colour.main()
        elif args == 4:
            from Options import Fruit
            Fruit.main()
        elif args == 5:
            from Options import Shapes
            Shapes.main()
        elif args == 6:
            from Options import Vegetable
            Vegetable.main()
        elif args == 7:
            from Options import Vehicles
            Vehicles.main()
 
    def option():
 
        lab_img1 = Button(
            main_window,
            image=img1,
            bg='#e6fff5',
            border=0,
            justify='center',
 
        )
        sel_btn1 = Button(
            text="Animals",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(1),
        )
 
        sel_btn2 = Button(
            text="Body parts",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(2),
        )
 
        sel_btn3 = Button(
            text="Colour",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(3),
        )
 
        sel_btn4 = Button(
            text="Fruits",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(4),
        )
 
        sel_btn5 = Button(
            text="Shapes",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(5),
        )
 
        sel_btn6 = Button(
            text="Vegetable",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(6),
        )
 
        sel_btn7 = Button(
            text="Vehicles",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="green",
            cursor="hand2",
            command=lambda: start_game(7),
        )
        lab_img1.grid(row=0, column=0, padx=20)
        sel_btn1.grid(row=0, column=4, pady=(10, 0), padx=50, )
        sel_btn2.grid(row=1, column=4, pady=(10, 0), padx=50, )
        sel_btn3.grid(row=2, column=4, pady=(10, 0), padx=50, )
        sel_btn4.grid(row=3, column=4, pady=(10, 0), padx=50, )
        sel_btn5.grid(row=4, column=4, pady=(10, 0), padx=50, )
        sel_btn6.grid(row=5, column=4, pady=(10, 0), padx=50, )
        sel_btn7.grid(row=6, column=4, pady=(10, 0), padx=50, )
 
    def show_option():
        start_btn.destroy()
 
        lab_img.destroy()
        option()
 
    main_window = Tk()
 
    main_window.geometry("500x500+500+150")
    main_window.resizable(0, 0)
    main_window.title("IT SOURCECODE --->> Jumbled Words Quiz")
    main_window.configure(background="#e6fff5")
 
    img0 = PhotoImage(file="logo1.png")
    img1 = PhotoImage(file="back.png")
 
    lab_img = Label(
        main_window,
        image=img0,
        bg='#e6fff5',
    )
    lab_img.pack(pady=(50, 0))
 
    start_btn = Button(
        main_window,
        text="Start",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="green",
        font=("", 13),
        cursor="hand2",
        command=show_option,
    )
    start_btn.pack(pady=(50, 20))
 
    main_window.mainloop()
 
 
start_main_page()
 