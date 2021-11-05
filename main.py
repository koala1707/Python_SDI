from interactive_console_client import InteractiveConsoleClient
from question_answer_manager import QuestionAnswerManager


def main(candidates_path, questions_log_path):
    manager = QuestionAnswerManager(candidates_path, questions_log_path)
    client = InteractiveConsoleClient(manager)
    client.run()


if __name__ == '__main__':
    main("faq.json", "asked_questions_log.txt")
