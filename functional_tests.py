

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):  
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
             
    def test_can_start_a_list_and_retrieve_it_later(self):
        
        # Edith ouviu falar de uma aplicação online interessante para
        # lista de tarefas. Ela decide verificar sua homepage
        self.browser.get('http://localhost:8000')  # noqa:F821

        # Ela percebe que o titulo da página e o cabeçalho mencionam listas
        # de tarefas (to-do)

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # Ela é convidada a inserir um item de tarefa imadiatamente

# Ela digita "Buy peacock feathers" (comprar penas de pavão) em uma caixa
# de texto (o hobby de Edith é fazer iscas para pesca com fly)

# Quando ela tecla enter, a página é atualizada, e agora a página lista
# "1: Buy peacock feathers" como um item em uma lista de tarefas

# Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro
# item. Ela insere "Üse peacock feathers to make a fly"
# (usar penas de pavão para fazer um fly - Edith é bem metódica)

# A página é atualizada novamnente a agora mostra dois itens em sua lista

# Edith se pergunta se o site lembrará de sua lista. Então ela nota
# que o site gera um url único para ela -- há um pequeno
# texto explicativo para isso.

# Ela acessa esse URL - sua lista de tarefas continua lá

# Satisfeita ela volta a dormmir


if __name__ == '__main__':
    unittest.main(warnings='ignore')
