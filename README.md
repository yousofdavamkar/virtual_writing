<h1 align="center">Virtual Handwriting to Text Converter</h1>

<p align="center">
  <strong>Project Topic:</strong> Converting Virtual Handwriting to Readable Text File<br>
  <strong>Student:</strong> Yousof Davamkar
</p>

<h2>Abstract</h2>

<p>This software, written in Python, allows users to write text in free space using hand gesture recognition and image processing. The written text can then be saved as a readable file.</p>

<h2>Table of Contents</h2>

<ol>
  <li><a href="#1-problem-definition">Problem Definition</a>
    <ul>
      <li><a href="#11-definition-of-writing">Definition of Writing</a></li>
      <li><a href="#12-research-objectives">Research Objectives</a></li>
    </ul>
  </li>
  <li><a href="#2-tools-used">Tools Used</a>
    <ul>
      <li><a href="#21-python">Python</a></li>
      <li><a href="#22-numpy">NumPy</a></li>
      <li><a href="#23-opencv">OpenCV</a></li>
      <li><a href="#24-mediapipe">Mediapipe</a></li>
      <li><a href="#25-api">API</a></li>
    </ul>
  </li>
  <li><a href="#3-program-guide">Program Guide</a></li>
  <li><a href="#references">References</a></li>
</ol>

<h2 id="1-problem-definition">1. Problem Definition</h2>

<h3 id="11-definition-of-writing">1.1 Definition of Writing</h3>

<p>Writing is an action through which humans visually represent their thoughts using script. These thoughts can take various written forms, including scientific, literary, and formal (administrative) texts. The invention of writing was a significant step in human civilization, marking the beginning of human progress. The primary reason for writing can be attributed to the human fear of forgetting and the need to record events and knowledge.</p>

<p>Writing is a process that allows for the analysis, review, and revision of information and ideas. It can be used as a tool for reasoning, inference, and clarification.</p>

<h3 id="12-research-objectives">1.2 Research Objectives</h3>

<p>As mentioned in the definition of writing, we need to record information in the age of communication. Today, there are many methods for recording information, but if we can achieve this goal without any need for nature, paper, and pen, it will improve resource management.</p>

<h2 id="2-tools-used">2. Tools Used</h2>

<h3 id="21-python">2.1 Python 3.7</h3>

<p>Python is an object-oriented, interpreted, high-level, and general-purpose programming language designed by Guido van Rossum and first released in 1991. The main design philosophy of Python is "high code readability," and it uses significant whitespace.</p>

<h3 id="22-numpy">2.2 NumPy</h3>

<p>NumPy is a Python library used for working with arrays. It also has functions for working in the domain of linear algebra, Fourier transform, and matrices. NumPy was created in 2005 by Travis Oliphant. It is an open-source project and you can use it freely.</p>

<h3 id="23-opencv">2.3 OpenCV</h3>

<p>OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in commercial products.</p>

<h3 id="24-mediapipe">2.4 MediaPipe</h3>

<p>MediaPipe is a cross-platform framework for building multimodal applied machine learning pipelines. It's a hand gesture recognition module launched by Google.</p>

<h3 id="25-api">2.5 API</h3>

<p>An Application Programming Interface (API) is a set of definitions and protocols for building and integrating application software. It lets products and services communicate with other products and services without having to know how they're implemented.</p>

<h2 id="3-program-guide">3. Program Guide</h2>

<ol>
  <li>Clone the program file from the following GitHub link:
    <pre><code>https://github.com/yousofdavamkar/virtual_writing.git</code></pre>
  </li>
  <li>Install all the software requirements listed in the <code>requirements.txt</code> file.</li>
  <li>Open a terminal in the program location and run the following command:
    <pre><code>python main.py</code></pre>
  </li>
  <li>After executing the above command, the software window will open.</li>
  <li>The default mode is eraser.</li>
  <li>To change and use available colors, use your index and middle fingers to hover over the desired color, and it will be automatically selected.</li>
  <li>Write your desired text with the selected color.</li>
  <li>Then, open your palm towards the camera to save the writing.</li>
  <li>After saving, a new window will open.</li>
  <li>At this stage, press the enter key and wait for the initial window to reopen.</li>
</ol>

<p>After a few moments, an image file of the above text will be saved in the <code>savedPaintings</code> folder, and a converted readable text file will be saved in the <code>convertedToText</code> folder.</p>

<h2 id="references">References</h2>

<ol>
  <li><a href="https://github.com/Severus11/Virtual-Air-Painting">https://github.com/Severus11/Virtual-Air-Painting</a></li>
  <li><a href="https://opencv.org">https://opencv.org</a></li>
  <li><a href="https://pypi.org/project/mediapipe">https://pypi.org/project/mediapipe</a></li>
  <li><a href="https://www.eboo.ir">https://www.eboo.ir</a></li>
</ol>
