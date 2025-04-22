import re
from collections import Counter
import zipfile


class BaseAnalyzer:
    """
        Developer Pavel Zdor
        date: 20.04.2025
        class of base analyzer of sequence
        """
    def __init__(self,  text):
        self._text = text

    def count_sentences(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            function of counting sentences
            """
        sentences = re.split(r'[.!?]', self._text)
        num = 1
        if len(sentences) != 1:
            num = len(sentences) - 1
        return num

    def count_narrative_sentences(self):

        num = re.findall(r'[А-ЯA-Z][^.!?]*[.]', self._text)
        return num

    def count_interrogative_sentences(self):
        num = re.findall(r'[А-ЯA-Z][^.!?]*[?]', self._text)
        return num

    def count_imperative_sentences(self):
        num = re.findall(r'[А-ЯA-Z][^.!?]*!', self._text)
        return num

    def calculate_avg_sen_length(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            calculating of average sentence length
            """
        sentences = re.split(r'[.!?]+', self._text)
        num_sentences = len(sentences)
        total_sentences_length = 0
        for sentence in sentences:
            words = re.findall(r'\b\w+\b', sentence)
            total_sentences_length += sum(len(word) for word in words)
        average_sentence_length = total_sentences_length / num_sentences
        return average_sentence_length

    def calculate_average_word_length(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            calculating of average word length
            """
        words = re.findall(r'\b\w+\b', self._text)
        total_word_length = sum(len(word) for word in words)
        average_word_length = total_word_length / len(words)
        return average_word_length

    def analyze_on_smiles(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            calculating of average word length
            """
        number_of_smiles = re.findall(r'[;:]-*[()\[\]]+', self._text)
        return len(number_of_smiles)

    def count_number_dv(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            calculating of binary numbers
            """
        cnt = re.findall(r'[01]+', self._text)
        return cnt

    def count_vowel_notvowel(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            calculating words witch starting of vowel and then not_vowel
            """
        cnt = re.findall(r'\b[АаЕеЁёИиОоУуЫыЭэЮюЯяAaEeIiOoUu][^АаЕеЁёИиОоУуЫыЭэЮюЯяAaEeIiOoUu\W\d]\w*\b', self._text)
        return cnt

    def count_vowel(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            calculating words witch starts and ends by vowels
            """
        cnt = re.findall(r'\b[АаЕеЁёИиОоУуЫыЭэЮюЯяAaEeIiOoUu]\w*|\w*[АаЕеЁёИиОоУуЫыЭэЮюЯяAaEeIiOoUu]\b', self._text)
        return cnt

    def count(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            calculating of amount of every symbol
            """
        matches = re.findall(r'.', self._text)
        char_count = Counter(matches)
        return char_count

    def count_after_symbol(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            calculating of words after , in alphabetical order
            """
        pattern = r',\s*([а-яa-z]+)'
        matches = re.findall(pattern, self._text)
        sorted_words = sorted(matches)
        return sorted_words


def create_zip_archive(output_file, file_to_archive):
    """
        Developer Pavel Zdor
        date: 20.04.2025
        create zip archive
        """
    # Creates a zip archive containing the provided file
    with zipfile.ZipFile(output_file, 'w', compression=zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.write(file_to_archive)
        archive_info = zip_file.getinfo(file_to_archive)
        print("Информация о файле в архиве:")
        print(f"Имя файла: {archive_info.filename}")
        print(f"Размер файла: {archive_info.file_size} байт")
        print(f"Сжатый размер: {archive_info.compress_size} байт")
        print(f"Коэффициент сжатия: {archive_info.file_size / archive_info.compress_size:.1f}x")


def write_file(output_file, content):
    """
        Developer Pavel Zdor
        date: 20.04.2025
        writes to output file
        """
    with open(output_file, "w") as file:
        file.write(content)


class DataWorker(BaseAnalyzer):
    # Class for working with data, inherits from TextAnalyzer
    def __init__(self, text):
        # Initializes the DataWorker with an input file and text
        super().__init__(text)
        self.text = text

    def analyze_text(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            displaying result of base analyze functions
            """
        # Analyzes the text and returns the analysis results as a string
        num_sentences = self.count_sentences()
        num_narrative_sentences = self.count_narrative_sentences()
        num_interrogative_sentences = self.count_interrogative_sentences()
        num_imperative_sentences = self.count_imperative_sentences()
        average_sentence_length = self.calculate_avg_sen_length()
        average_word_length = self.calculate_average_word_length()
        num_smileys = self.analyze_on_smiles()
        after_symbol = self.count_after_symbol()
        dv = self.count_number_dv()
        end_on_vowel = self.count_vowel()
        vowel_nv = self.count_vowel_notvowel()
        dictt = self.count()
        output_content = ""
        output_content += "Количество предложений в тексте: {}\n".format(num_sentences)
        output_content += "Количество повествовательных предложений: {}\n".format(len(num_narrative_sentences))
        output_content += "Количество вопросительных предложений: {}\n".format(len(num_interrogative_sentences))
        output_content += "Количество побудительных предложений: {}\n".format(len(num_imperative_sentences))
        output_content += "Средняя длина предложения в символах: {}\n".format(average_sentence_length)
        output_content += "Средняя длина слова в символах: {}\n".format(average_word_length)
        output_content += "Количество смайликов в тексте: {}\n".format(num_smileys)
        output_content += "Список после запятой в алфавитном порядке: {}\n".format(after_symbol)
        output_content += "Список двоичных чисел: {}\n".format((dv))
        output_content += "Слова заканчивающиеся на гласную: {}\n".format(end_on_vowel)
        output_content += "Список слов, у которых первая буква гласная, а вторая – согласная.: {}\n".format(vowel_nv)
        output_content += "Сколько раз повторяется каждый символ: {}\n".format(dictt)
        return output_content

