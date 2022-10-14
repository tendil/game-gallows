from game import Game
from game_status import GameStatus


def chars_list_to_str(chars):
	return ''.join(chars)

HANGMAN_PICS = '''
Добро пожаловать в Весилицу! xD)
---------------------------------
Попробуй угадать слова по буквам.
			+---+
			0 	|
		   /|\ 	|
		   / \ 	|
		  =======
	'''

game = Game()
word = game.generate_word()

letters_count = len(word)

print(HANGMAN_PICS)

print(f'Слово состоит из -- {letters_count} -- букв. \n')
print('Попробуй угадать слова по буквам.')

while game.game_status == GameStatus.IN_PROGRESS:
	letter = input('Введи свою букву - ')
	state = game.guess_letter(letter)

	print(chars_list_to_str(state))

	print(f'Оставшиеся попытки = {game.remaining_tries}')
	print(f'Использованные буквы: {chars_list_to_str(game.tried_letters)}')

if game.game_status == GameStatus.LOST:
	print(30 * '-', f'\nТы повешен!\n' + 30 * '-')
	print(f'Загаданное слово: {game.word}')
else:
	print('На этот раз помилуем тебя, вешать не будем, ты победил!')
