# Mock CodeSignal Pre-screen: INDUSTRY CODING FRAMEWORK

This serves as a mock example of an industry coding framework assessment, similar to those found in pre-screens on CodeSignal. It's important to highlight the rarity of comprehensive guides or examples on navigating these types of assessments on the internet, making this document an invaluable resource for those seeking to prepare for such challenges 🚀.

For more insights and resources, follow the creator on Twitter [@PaulLockettkpb](https://twitter.com/PaulLockettkpb).

This guide is part of his journey in exploring and sharing knowledge within the coding community.

The tasks outlined in this document are crafted to emulate the complexity and breadth of coding assessments typically encountered during technical interviews or coding competitions 🧩. Each level introduces incrementally more complex problems, requiring a solid understanding of data structures, algorithms, and software engineering principles 📚.

## Pre-requisites

Before diving into the tasks and running the tests outlined in this guide, it's crucial to ensure that your development environment is properly set up. Here are the prerequisites necessary to run the test and simulation effectively:

1. **Python Installation**: Ensure that you have Python installed on your machine. This guide and the accompanying code are designed to work with Python 3.6 or newer. You can download Python from the official website at [python.org](https://www.python.org/downloads/). After installation, you can verify the installation by running `python --version` or `python3 --version` in your terminal or command prompt.

> **Important Note**: CodeSignal utilizes Python Version **3.10.6** for its assessments.

3. **Familiarity with Terminal or Command Prompt**: Basic knowledge of using the terminal (Mac/Linux) or command prompt (Windows) will be beneficial. You will need to use it to run the test scripts provided in the `test_simulation.py` file.

4. **Install Required Python Packages**: Before starting with the tasks, it's essential to install the Python packages listed in the `requirements.txt` file. These packages include necessary libraries that might be used throughout the tasks in this guide. To install these packages, run the following command in your terminal or command prompt:
   ```
   pip install -r requirements.txt
   ```
   or
   ```
   /path/to/python3.10.6 -m pip install -r requirements.txt
   ```
   This command tells pip, Python's package installer, to install all the packages listed in the `requirements.txt` file. Ensure you are in the same directory as the `requirements.txt` file when running this command or provide the correct path to it. Installing these packages beforehand will ensure that you have all the necessary tools and libraries at your disposal, facilitating a smoother coding experience.
   > **Important Note**: When installing Python and the required packages, it is crucial to ensure that the version of Python installed matches the version used by CodeSignal, which is **3.10.6**. Additionally, verify that your Integrated Development Environment (IDE) is configured to use the same Python interpreter. This consistency is essential for avoiding discrepancies in behavior or functionality due to differences in Python versions.

By ensuring these prerequisites are met, you will be well-prepared to engage with the tasks, run tests, and make the most out of this mock CodeSignal pre-screen assessment. Remember, a well-set-up development environment is key to a smooth and efficient coding experience.

## How to Use This Mock Assessment

1. **Timing**: Set a strict time limit of 90 minutes for yourself to complete the tasks ⏳. This practice is designed to simulate the time constraints often present in real assessments, fostering the development of effective time management skills.
2. **Sequential Progression**: Start with Level 1 and do not advance to the subsequent level until you have fully completed the preceding one 🛤️. This methodical approach ensures a gradual and thorough understanding of the challenges presented.

3. **Testing and Development Environment**: Focus your coding efforts within the `simulation.py` file 🖥️. This file is where you will implement your solutions and simulate the operations described in the tasks.

4. **Running Tests**: Utilize the provided `test_simulation.py` file to run unit tests against your code 🧪. This file contains test cases for each level, allowing you to verify the correctness of your solutions incrementally. To run the tests for a specific level, use the following command structure in your terminal or command prompt:

   - For Level 1 tests: `python3 -m unittest test_simulation.TestSimulateCodingFramework.test_group_1`
   - For Level 2 tests: `python3 -m unittest test_simulation.TestSimulateCodingFramework.test_group_2`
   - For subsequent levels, adjust the `test_group_x` part of the command accordingly.

5. **Refactoring**: As you progress through the levels, revisit and refactor your earlier solutions as needed to accommodate the additional functionality required by later tasks 🔧. This iterative process is key to developing scalable and maintainable software.

To ensure the fastest possible progression through the levels, consider the following strategies:

1. **Familiarize Yourself with the Framework**: Before starting the timer, spend some time understanding the coding framework and the structure of the tasks (see the pdf in this repo) 📖. This upfront investment will pay dividends by reducing the time needed to interpret tasks during the timed session.

2. **Plan Before You Code**: For each task, spend a few minutes planning your approach before you start coding 📝. This can include writing pseudocode, drawing diagrams, or outlining the steps you need to take. A clear plan will help you code more efficiently and reduce the time spent on debugging.

3. **Practice Speed Typing**: The physical act of typing can be a bottleneck 🚀. Improving your typing speed through practice can have a surprisingly significant impact on your overall speed.

4. **Master the Art of Skimming**: Learn to quickly skim the task descriptions to identify the key requirements and constraints 🔍. This skill will allow you to start formulating your solution even as you finish reading the task.

5. **Utilize Code Snippets and Libraries**: Where appropriate, use code snippets and libraries to avoid reinventing the wheel 🛠️. However, be cautious not to waste time trying to force a library to do something it's not well-suited for.

6. **Parallelize Testing and Coding**: If possible, set up your environment so you can run tests on the code you've already written while continuing to work on other parts of the task 🔄. This can help identify issues early and reduce overall development time.

7. **Focus on Passing Tests Over Perfection**: Aim to get a working solution as quickly as possible, even if it's not the most elegant 🎯. You can always refactor later if you have time remaining.

By incorporating these strategies, you can significantly increase your speed and efficiency, allowing you to progress through the levels at an accelerated pace ⚡.

The following table, sourced from [How hackable are automated coding assessments?](https://yanirseroussi.com/2023/05/26/how-hackable-are-automated-coding-assessments/), offers a detailed breakdown of the expected time allocation for questions within Industry Coding Assessments. It is formatted for clear understanding and reference:

| Level | Expected Time (minutes) |
| ----- | ----------------------- |
| 1     | 10-15                   |
| 2     | 20-30                   |
| 3     | 30-60                   |
| 4     | 30-60                   |

When aggregating the time ranges across all levels, the cumulative estimate to complete the assessment ranges from 90 to 165 minutes. However, the stipulated completion time for candidates is set at 90 minutes. This discrepancy is intentional and serves a specific purpose as outlined below:

> The assessment's maximum allowed completion time is capped at 90 minutes. This constraint is not an expectation for candidates to solve all tasks within this limit. The rationale behind shorter assessments, despite their potential for a more accurate measurement of candidate skills, is rooted in the observation that candidate willingness to engage with the assessment drops significantly for tests exceeding 2 hours in duration. A critical aspect of evaluating candidates' capabilities lies in observing the extent of their progression within the allocated timeframe, rather than the completion of all tasks.

Adhering to these guidelines and completing the tasks within the designated time frame will equip you with practical experience in tackling coding assessments.

Best of luck, and remember to frequently test your solutions to track your progress and obtain feedback on your approach 🍀.

## How to Contribute

Contributing to this guide is a fantastic way to help others prepare for industry coding assessments. If you're interested in adding more questions and challenges, we welcome your contributions! Here's how you can contribute:

1. **Understand the Framework**: Before creating new questions, please familiarize yourself with the existing coding framework and the structure of the tasks. Refer to the PDF in this repository for detailed guidelines on how questions should be structured and what they aim to assess.

2. **Create New Questions**: Design your questions to mimic real-world coding assessments. Ensure they are clear, concise, and cover a range of difficulties. Each question should challenge a specific skill or set of skills relevant to coding assessments, such as algorithmic thinking, data structures, or problem-solving under time constraints.

3. **Follow the Existing Structure**: Your questions should be similar in structure (but not content) to the ones found in the `Practice Assessments` directory, specifically the `file_storage` example. This consistency helps candidates familiarize themselves with the format and focus on solving the problems.

4. **Adhere to the PDF Guidelines**: The PDF in the repository outlines the rules for how questions should work. Please ensure your questions comply with these rules to maintain the quality and relevance of the assessments.

5. **Submit Your Questions**: Once you have created your questions, place them in the `Practice Assessments` directory. If your questions are based on a new theme or concept not currently covered, consider creating a new subdirectory within `Practice Assessments` to organize them accordingly.

6. **Open a Pull Request**: Submit your contributions via a pull request. In your pull request, provide a brief explanation of your questions and how they align with the objectives of the coding framework. Our team will review your submission and provide feedback if necessary.

7. **Stay Engaged**: After submitting your questions, stay engaged with the community. Respond to feedback on your pull request and be open to making adjustments to your questions as recommended by reviewers.

By contributing to this guide, you're not only helping others prepare for their coding assessments but also honing your own skills in creating meaningful, challenging coding problems. We look forward to seeing your contributions and expanding our collection of practice assessments!
