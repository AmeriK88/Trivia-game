import tkinter as tk
from tkinter import simpledialog, messagebox
import random

class TriviaGame:
    def __init__(self, window):
        self.window = window
        self.categories = {
            'ciencia': [
                ("¿Cuál es el símbolo químico del oxígeno?", ["A) O", "B) Ox", "C) O2", "D) O3"], "A) O"),
                ("¿Cuál es la fórmula química del agua?", ["A) H2O", "B) CO2", "C) O2", "D) H2"], "A) H2O"),
                ("¿Dónde se encuentran los huesos más pequeños del cuerpo?", ["A) La mano", "B) El pie", "C) La oreja", "D) La nariz"], "C) La oreja"),
                ("¿Cuántos corazones tiene un pulpo?", ["A) 1", "B) 2", "C) 3", "D) 4"], "C) 3"),
                ("¿Cuál es la sustancia natural más dura de la Tierra?", ["A) Oro", "B) Calcio", "C) Hierro", "D) Diamante"], "D) Diamante"),
                ("Aproximadamente, ¿cuánto tarda la luz del sol en llegar a la Tierra?", ["A) 8 minutos", "B) 1 Minuto", "C) 8 segundos", "D) 1 segundo"], "A) 8 minutos"),
                ("¿Cuántos huesos hay en el cuerpo humano?", ["A) 150", "B) 206", "C) 301", "D) 522"], "B) 206"),
                ("Este es el único tipo de canino que puede trepar a los árboles.", ["A) Zorro gris", "B) Lobo Ibérico", "C) Pastor Belga", "D) Chihuahua"], "A) Zorro gris"),               
            ],
            'deportes': [
                ("¿En qué deporte se utiliza una raqueta?", ["A) Fútbol", "B) Tenis", "C) Baloncesto", "D) Golf"], "B) Tenis"),
                ("¿Cuántos jugadores hay en un equipo de fútbol?", ["A) 11", "B) 10", "C) 9", "D) 12"], "A) 11"),  
                ("¿Cuál es el evento deportivo más antiguo del mundo que aún se celebra?", ["A) Juegos Olímpicos", "B) Mundial Fútbol", "C) Mundial F1", "D) FIFA"], "A) Juegos Olímpicos"),
                ("¿Quién es el corredor más rápido de la historia en los 100 metros lisos?", ["A) Jimmy Fallon", "B) Lewis Johnson", "C) Cart Lewis", "D) Usain Bolt"], "D) Usain Bolt"),
                ("¿Qué país ganó la Copa del Mundo de la FIFA más veces?", ["A) Argentina", "B) Brazil", "C) Francia", "D) Alemania"], "B) Brazil"),
                ("¿Cuál es el deporte más popular del mundo?", ["A) Esquiar", "B) Baloncesto", "C) Baseball", "D) Fútbol"], "D) Fútbol"),             
            ],
            'historia': [
                ("¿Quién fue el primer presidente de los Estados Unidos?", ["A) George Washington", "B) Thomas Jefferson", "C) Abraham Lincoln", "D) Benjamin Franklin"], "A) George Washington"),
                ("¿En qué año cayó el Muro de Berlín?", ["A) 1989", "B) 1991", "C) 1987", "D) 1990"], "A) 1989"),  
                ("¿Quién es el inventor de la luz eléctrica?", ["A) Thomas Jackson", "B) Thomas Edison", "C) Jerry Lewis", "James Ferguson"], "B) Thomas Edison"),
                ("¿Quién fue el primer hombre en caminar sobre la luna?", ["A) Johnny Cash", "Ethan Hawke", "C) Neil Armstrong", "D) James Dean"], "C) Neil Armstrong"),
                ("¿En qué año fue asesinado John F. Kennedy?", ["A) 1963", "B) 1991", "C) 1976", "D) 1930"], "A) 1963"),
                ("¿Cuándo comienza la Primera Guerra Mundial?", ["A) 1989", "B) 1914", "C) 1941", "D) 1890"], "B) 1914"),  
                ("¿Quién pronunció el famoso discurso “Tengo un sueño”?", ["A) Alfred Hitchcock", "B) James Patterson", "C) Martin Luther King", "D) Malcom X"], "C) Martin Luther King"),        
            ]
        }
        self.score = 0
        self.current_question = 0
        self.questions = []
        self.correct_answer = ""
        self.playing = False
        self.finished_all_questions = False

    def welcome_user(self):
        self.name = simpledialog.askstring("Nombre", "¡Bienvenido al juego de trivia! Por favor, ingresa tu nombre: ")
        messagebox.showinfo("Bienvenido", f"¡Hola, {self.name}! Bienvenido a Trivia!")

    def ask_to_play(self):
        response = messagebox.askyesno("Jugar", "¿Quieres jugar?")
        return response

    def choose_category(self):
        category = simpledialog.askstring("Categoría", "Elige una categoría: ciencia, deportes, historia")
        self.questions = self.categories.get(category, [])
        random.shuffle(self.questions)

    def ask_question(self):
        if self.current_question < len(self.questions):
            question, options, self.correct_answer = self.questions[self.current_question]
            self.current_question += 1
            self.question_label.config(text=question)
            for i in range(4):
                self.option_buttons[i].config(text=options[i], state="normal")
        else:
            messagebox.showinfo("Fin de la categoría", f"¡Has terminado la categoría! Tu puntuación actual es: {self.score}")
            if self.playing:
                if self.finished_all_categories():
                    messagebox.showinfo("Fin del juego", f"¡Has respondido todas las preguntas! Tu puntuación final es: {self.score}")
                    self.play_again()
                else:
                    self.choose_category()
                    self.current_question = 0  # Reiniciamos el índice de la pregunta actual
                    self.ask_question()  # Volvemos a empezar con las preguntas de la nueva categoría
            else:
                messagebox.showinfo("Fin del juego", f"¡Has terminado el juego! Tu puntuación final es: {self.score}")
                self.play_again()

    def finished_all_categories(self):
        for category_questions in self.categories.values():
            if not all(question in self.questions for question, _, _ in category_questions):
                return False
        return True

    
    def check_answer(self, answer):
        if answer == self.correct_answer:
            self.score += 1
            messagebox.showinfo("Correcto", "¡Correcto!")
        else:
            self.score = max(0, self.score - 1)
            messagebox.showinfo("Incorrecto", "¡Incorrecto!")
        self.score_label.config(text=f"Puntuación: {self.score}")
        self.ask_question()

    def play_again(self):
        play_again = messagebox.askyesno("Jugar de nuevo", "¿Quieres jugar de nuevo?")
        if play_again:
            self.score = 0
            self.score_label.config(text=f"Puntuación: {self.score}")
            self.finished_all_questions = False
            self.choose_category()
            self.current_question = 0  # Reiniciamos el índice de la pregunta actual
            self.ask_question()  # Empezamos con las preguntas de la nueva partida
        else:
            self.window.quit()

    def play(self):
        self.playing = True
        self.question_label = tk.Label(self.window, text="", bg="lightgreen", fg="black", font=("Arial", 14, "bold"))
        self.question_label.pack(pady=10)
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.window, text="", command=lambda i=i: self.check_answer(self.option_buttons[i].cget("text")), state="disabled", bg="lightblue", fg="black", font=("Arial", 12))
            button.pack(pady=5, padx=10, ipadx=10, ipady=5, fill=tk.X)
            self.option_buttons.append(button)
        self.score_label = tk.Label(self.window, text=f"Puntuación: {self.score}", bg="lightgreen", fg="black", font=("Arial", 12, "bold"))
        self.score_label.pack(pady=10)

        self.ask_question()

window = tk.Tk()
window.title("Trivia Game")
game = TriviaGame(window)
game.welcome_user()
if game.ask_to_play():
    game.choose_category()
    game.play()
else:
    print("¡Hasta la próxima!")
window.mainloop()





















