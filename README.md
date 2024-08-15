## AWS GenScribe: Elevate Your Essay Craft

**AWS GenScribe** is an advanced essay crafting tool that leverages the power of Amazon Bedrock and the Anthropic Claude 3 Sonnet model, integrated through LangChain and Streamlit, to provide users with a sophisticated platform for essay writing. This tool is designed to assist users in generating, refining, and enhancing their essays by utilizing state-of-the-art AI models. Whether you are a student, a researcher, or a professional writer, AWS GenScribe offers a seamless and intuitive experience that elevates the quality of your written work.

### Key Features:
- **AI-Powered Writing Assistance**: Utilize the Claude 3 Sonnet model for generating content, offering suggestions, and improving the overall quality of essays.
- **User-Friendly Interface**: Built on Streamlit, the platform provides an easy-to-navigate interface, ensuring that users can focus on their writing without technical distractions.
- **Customizable Prompts**: Fine-tune the AI's responses to align with specific writing styles, tones, and requirements.
- **Real-Time Editing**: Make adjustments to your content in real time, with immediate feedback from the AI model.

---

## Step-by-Step Setup Instructions

### 1. Install Python
Ensure you have Python installed on your system. If not, follow the official [Python installation guide](https://docs.python-guide.org/starting/install3/linux/).

### 2. Setup Python Environment
Create a virtual environment to manage dependencies and isolate your project’s packages. Follow the instructions provided [here](https://docs.python-guide.org/starting/install3/linux/).

### 3. Setup AWS CLI
To interact with AWS services, you need the AWS Command Line Interface (CLI). Follow the [AWS CLI quickstart guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html) to set it up.

### 4. Clone the Repository
Download the project files by cloning the GitHub repository. Open a terminal and execute the following commands:
```bash
git clone https://github.com/awsstudygroup/Suggest-Writing
cd Suggest-Writing
```

### 5. Install Required Packages
Navigate to the project directory and install the necessary Python packages using the following command:
```bash
pip3 install -r requirements.txt
```

### 6. Run the Application
Start the Streamlit application by running the command below. This will launch the AWS GenScribe platform on your local server:
```bash
streamlit run Home.py --server.port 8080
```

### 7. Explore the Demo and Sample Data
- **Demo Videos**: Access the `demo` folder in the repository to view demonstration videos showcasing the features and capabilities of AWS GenScribe.
- **Sample Data**: Refer to the `samples` folder for sample essays and data to get started with your writing process.

---

## Architecture Overview

The architecture of AWS GenScribe is designed for scalability, efficiency, and ease of use. It integrates Amazon Bedrock with the Anthropic Claude 3 Sonnet model via LangChain, running on a Streamlit frontend. Below is a visual representation of the architecture:

![Architecture](./Architecture.png)

---

## Additional Resources

To further enhance your understanding of prompt design and the Claude 3 model, refer to the following resources:
- [Introduction to Prompt Design](https://docs.anthropic.com/claude/docs/introduction-to-prompt-design)
- [Claude 3 Model Card](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf)

