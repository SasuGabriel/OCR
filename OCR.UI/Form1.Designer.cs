namespace OCR.UI
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.label1 = new System.Windows.Forms.Label();
            this.ImageLoaded = new System.Windows.Forms.PictureBox();
            this.TextDetection = new System.Windows.Forms.RichTextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.LoadImage = new System.Windows.Forms.Button();
            this.DetectText = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.ImageLoaded)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(12, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(201, 20);
            this.label1.TabIndex = 0;
            this.label1.Text = "OCR Google Cloud Test";
            // 
            // ImageLoaded
            // 
            this.ImageLoaded.ErrorImage = ((System.Drawing.Image)(resources.GetObject("ImageLoaded.ErrorImage")));
            this.ImageLoaded.InitialImage = ((System.Drawing.Image)(resources.GetObject("ImageLoaded.InitialImage")));
            this.ImageLoaded.Location = new System.Drawing.Point(12, 65);
            this.ImageLoaded.Name = "ImageLoaded";
            this.ImageLoaded.Size = new System.Drawing.Size(372, 360);
            this.ImageLoaded.TabIndex = 1;
            this.ImageLoaded.TabStop = false;
            // 
            // TextDetection
            // 
            this.TextDetection.Location = new System.Drawing.Point(420, 65);
            this.TextDetection.Name = "TextDetection";
            this.TextDetection.Size = new System.Drawing.Size(368, 361);
            this.TextDetection.TabIndex = 2;
            this.TextDetection.Text = "";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 12.25F);
            this.label2.Location = new System.Drawing.Point(12, 42);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(108, 20);
            this.label2.TabIndex = 3;
            this.label2.Text = "Image loaded";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 12.25F);
            this.label3.Location = new System.Drawing.Point(421, 42);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(114, 20);
            this.label3.TabIndex = 4;
            this.label3.Text = "Text detection";
            // 
            // LoadImage
            // 
            this.LoadImage.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.LoadImage.Location = new System.Drawing.Point(16, 432);
            this.LoadImage.Name = "LoadImage";
            this.LoadImage.Size = new System.Drawing.Size(368, 37);
            this.LoadImage.TabIndex = 5;
            this.LoadImage.Text = "Load image/receipt/etc";
            this.LoadImage.UseVisualStyleBackColor = true;
            this.LoadImage.Click += new System.EventHandler(this.LoadImage_Click);
            // 
            // DetectText
            // 
            this.DetectText.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.DetectText.Location = new System.Drawing.Point(420, 432);
            this.DetectText.Name = "DetectText";
            this.DetectText.Size = new System.Drawing.Size(368, 37);
            this.DetectText.TabIndex = 6;
            this.DetectText.Text = "Detect text";
            this.DetectText.UseVisualStyleBackColor = true;
            this.DetectText.Click += new System.EventHandler(this.DetectText_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 471);
            this.Controls.Add(this.DetectText);
            this.Controls.Add(this.LoadImage);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.TextDetection);
            this.Controls.Add(this.ImageLoaded);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.ImageLoaded)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.PictureBox ImageLoaded;
        private System.Windows.Forms.RichTextBox TextDetection;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Button LoadImage;
        private System.Windows.Forms.Button DetectText;
    }
}

