using Google.Cloud.Vision.V1;
using System;
using System.Drawing;
using System.Windows.Forms;

namespace OCR.UI
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // write the path for the configuration path from google here
        public static string filePath = "path-to-config-file-from-google-cloud-OCR-api";

        private void LoadImage_Click(object sender, EventArgs e)
        {
            OpenFileDialog open = new OpenFileDialog();
            if (open.ShowDialog() == DialogResult.OK)
            {
                ImageLoaded.Image = new Bitmap(open.FileName);
                ImageLoaded.SizeMode = PictureBoxSizeMode.StretchImage;
                filePath = open.FileName;
            }
        }

        private void DetectText_Click(object sender, EventArgs e)
        {
            try
            {
                TextDetection.Text = "";

                var client = ImageAnnotatorClient.Create();
                var image = Google.Cloud.Vision.V1.Image.FromFile(filePath);

                var response = client.DetectText(image);
                foreach (var annotation in response)
                {
                    if (annotation.Description != null)
                    {
                        TextDetection.Text += annotation.Description;
                        TextDetection.Text += System.Environment.NewLine;
                    }
                }
            }
            catch(Exception ex)
            {
                TextDetection.Text += "ERROR";
                TextDetection.Text += System.Environment.NewLine;
                TextDetection.Text += ex.Message;
            }
        }
    }
}
