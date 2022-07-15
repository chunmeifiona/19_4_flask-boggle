from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def test_display_board(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn("<h1>Boggle Game!</h1>", html)
            self.assertIn('board', session)
            self.assertIsNone(session.get('highscore'))

    def test_check_valid_word(self):
        """test if word is valid in the transaction session board"""
        with app.test_client() as client:
            with client.session_transaction() as make_session_board_size:
                make_session_board_size['board_size'] = 5
            with client.session_transaction() as make_session_board:
                make_session_board['board'] = [['A','N','D','I','N'],
                                               ['A','N','D','I','N'],
                                               ['A','N','D','I','N'],
                                               ['A','N','D','I','N'],
                                               ['A','N','D','I','N']]

            res = client.get("/valid?guess_word=and")
            self.assertEqual(res.status_code,200)
            self.assertEqual(res.json['result'], 'ok')

            res = client.get("/valid?guess_word=not")
            self.assertEqual(res.status_code,200)
            self.assertEqual(res.json['result'], 'not-on-board')

            res = client.get("/valid?guess_word=gakghdjgdjfhja")
            self.assertEqual(res.status_code,200)
            self.assertEqual(res.json['result'], 'not-word')




