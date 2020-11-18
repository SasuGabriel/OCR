using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Threading.Tasks;
using System.Xml;

namespace Laborator6
{
    class ParserResult
    {
        public string Form { get; set; }
        public string Deprel { get; set; }
        public string Lemma { get; set; }
        public string Postag { get; set; }
    }

    class TaggerResult
    {
        public string WordLemma { get; set; }
        public string POS { get; set; }
    }


    class Program
    {
        public static List<ParserResult> ParserResults = new List<ParserResult>();
        public static List<TaggerResult> TaggerResultS = new List<TaggerResult>();

        public static void Display(ParserResult parserResult, int index)
        {
            Console.WriteLine($"{index}:   Form: {parserResult.Form}, Posttag: {parserResult.Postag}, Lemma: {parserResult.Lemma}, Deprel: {parserResult.Deprel}");
        }
        public static void Display(TaggerResult taggerResult, int index)
        {
            Console.WriteLine($"{index}:   WordLemma: {taggerResult.WordLemma}, POS: {taggerResult.POS}");
        }

        public static async Task ExtractWithTagger()
        {
            Console.WriteLine("Extracting with tagger....");

            XmlReaderSettings settings = new XmlReaderSettings();
            settings.IgnoreWhitespace = true;
            settings.Async = true;

            using (var fileStream = File.OpenText("Camil Petrescu - Ultima noapte de dragoste, intaia noapte de razboi_Tagger.xml"))
            using (XmlReader reader = XmlReader.Create(fileStream, settings))
            {
                while (reader.Read())
                {
                    switch (reader.NodeType)
                    {
                        case XmlNodeType.Element:
                            TaggerResultS.Add(new TaggerResult()
                            {
                                WordLemma = reader.GetAttribute("LEMMA"),
                                POS = reader.GetAttribute("POS")
                            }); ;
                            break;
                    }
                }
            }

            Console.WriteLine("Extracting with tagger finished.");
        }

        public static void ExtractWithParser()
        {
            Console.WriteLine("Extracting with parser....");

            XmlReaderSettings settings = new XmlReaderSettings();
            settings.IgnoreWhitespace = true;

            using (var fileStream = File.OpenText("Camil Petrescu - Ultima noapte de dragoste, intaia noapte de razboi_Parser.xml"))
            using (XmlReader reader = XmlReader.Create(fileStream, settings))
            {
                while (reader.Read())
                {
                    switch (reader.NodeType)
                    {
                        case XmlNodeType.Element:
                            ParserResults.Add(new ParserResult()
                            {
                                Form = reader.GetAttribute("form"),
                                Deprel = reader.GetAttribute("deprel"),
                                Lemma = reader.GetAttribute("lemma"),
                                Postag = reader.GetAttribute("postag")
                            });
                            break;
                    }
                }
            }

            Console.WriteLine("Extracting with parser finished");
        }

        public static List<string> Task1_Tokenize(string outputFileName)
        {
            var allWordsTokenized = new List<string>();

            if (File.Exists(outputFileName))
            {
                File.Delete(outputFileName);
            }

            Console.WriteLine($"Writing to file {outputFileName} started");

            using (StreamWriter sw = File.AppendText(outputFileName))
            {
                int i = 1;
                foreach (var wordTag in ParserResults)
                {
                    var word = wordTag.Form;
                    if (!string.IsNullOrEmpty(word) && !Char.IsPunctuation(word, 0))
                    {
                        allWordsTokenized.Add(wordTag.Form);
                        sw.WriteLine($"Word nr. {i} : " + wordTag.Form);
                        i++;
                    }
                }
            }

            Console.WriteLine($"Writing to file {outputFileName} finished");

            return allWordsTokenized;
        }

        public static List<string> Task2_Lemmatization(string outputFileName)
        {
            var allWordsLemmatized = new List<string>();

            if (File.Exists(outputFileName))
            {
                File.Delete(outputFileName);
            }

            Console.WriteLine($"Writing to file {outputFileName} started");

            using (StreamWriter sw = File.AppendText(outputFileName))
            {
                int i = 1;
                foreach (var wordTag in ParserResults)
                {
                    var lemmaWord = wordTag.Lemma;
                    if (!string.IsNullOrEmpty(lemmaWord) && !Char.IsPunctuation(lemmaWord, 0))
                    {
                        allWordsLemmatized.Add(lemmaWord);
                        sw.WriteLine($"Word lemmatized nr. {i} : " + lemmaWord);
                        i++;
                    }
                }
            }

            Console.WriteLine($"Writing to file {outputFileName} finished");

            return allWordsLemmatized;
        }

        public static List<string> Task3_POS(string outputFileName)
        {
            var allWordsPOSTagged = new List<string>();

            if (File.Exists(outputFileName))
            {
                File.Delete(outputFileName);
            }

            Console.WriteLine($"Writing to file {outputFileName} started");

            using (StreamWriter sw = File.AppendText(outputFileName))
            {
                int i = 1;
                foreach (var wordTag in TaggerResultS)
                {
                    var pos = wordTag.POS;
                    var WordLemma = wordTag.WordLemma;
                    if (!string.IsNullOrEmpty(pos) && !string.IsNullOrEmpty(WordLemma) && !Char.IsPunctuation(WordLemma, 0))
                    {
                        allWordsPOSTagged.Add(WordLemma  + " => " + pos);
                        sw.WriteLine($"{i} : {WordLemma} =>  {pos}");
                        i++;
                    }
                }
            }

            Console.WriteLine($"Writing to file {outputFileName} finished");

            return allWordsPOSTagged;
        }

        public static Dictionary<string, int> Task4_WordFrequency(string outputFileName, List<string> allWordsLemmatized)
        {
            var wordFrequencyDictionary = new Dictionary<string, int>();
            if (File.Exists(outputFileName))
            {
                File.Delete(outputFileName);
            }

            foreach (var wordLemma in allWordsLemmatized)
            {
                var wordIsInDictionary = wordFrequencyDictionary.ContainsKey(wordLemma);
                if (wordIsInDictionary)
                {
                    wordFrequencyDictionary[wordLemma] = ++wordFrequencyDictionary[wordLemma];
                }
                else
                {
                    wordFrequencyDictionary.Add(wordLemma, 1);
                }
            }

            wordFrequencyDictionary = wordFrequencyDictionary.OrderByDescending(x => x.Value).ToDictionary(pair => pair.Key, pair => pair.Value); 
            Console.WriteLine($"Writing to file {outputFileName} started");

            using (StreamWriter sw = File.AppendText(outputFileName))
            {
                int i = 1;
                foreach (var wordCount in wordFrequencyDictionary)
                {
                        sw.WriteLine($"{i} : {wordCount.Key} =>  {wordCount.Value}");
                        i++;
                }
            }

            Console.WriteLine($"Writing to file {outputFileName} finished");

            return wordFrequencyDictionary;
        }

        public static Dictionary<string, int> Task5_POSFrequency(string outputFileName, List<string> allPOS)
        {
            var posFrequencyDictionary = new Dictionary<string, int>();
            if (File.Exists(outputFileName))
            {
                File.Delete(outputFileName);
            }

            foreach (var posTag in allPOS)
            {
                var wordIsInDictionary = posFrequencyDictionary.ContainsKey(posTag);
                if (wordIsInDictionary)
                {
                    posFrequencyDictionary[posTag] = ++posFrequencyDictionary[posTag];
                }
                else
                {
                    posFrequencyDictionary.Add(posTag, 1);
                }
            }

            posFrequencyDictionary = posFrequencyDictionary.OrderByDescending(x => x.Value).ToDictionary(pair => pair.Key, pair => pair.Value);
            Console.WriteLine($"Writing to file {outputFileName} started");

            using (StreamWriter sw = File.AppendText(outputFileName))
            {
                int i = 1;
                foreach (var posCount in posFrequencyDictionary)
                {
                    sw.WriteLine($"{i} : {posCount.Key} =>  {posCount.Value}");
                    i++;
                }
            }

            Console.WriteLine($"Writing to file {outputFileName} finished");

            return posFrequencyDictionary;
        }

        static void Main(string[] args)
        {
            ExtractWithParser();
            ExtractWithTagger().GetAwaiter().GetResult();

            var wordsTokenized = Task1_Tokenize("task1_tokenize.txt");
            var wordsLemmatized = Task2_Lemmatization("task2_lemmatize.txt");
            var wordsPOSTagged = Task3_POS("task3_POSTagged.txt");
            var wordCountDictionary = Task4_WordFrequency("task4_wordCount.txt", wordsLemmatized);
            var posFoundList = new List<string>();
            foreach (var wordPOSTagged in wordsPOSTagged)
            {
                posFoundList.Add(wordPOSTagged.Split(" => ")[1]);
            }
            var posCountDictionary = Task4_WordFrequency("task5_POSCount.txt", posFoundList);
        }
    }
}
