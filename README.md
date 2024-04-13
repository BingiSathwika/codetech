# codetech
# TASK 1
TITLE: CodTech IT Solutions Internship - Task Documentation: “CHATBOT WITH RULE-BASED RESPONSES” Using PYTHON.

INTERN INFORMATION: 

Name: Bingi Sathwika

ID: C0D5077


INTRODUCTION

Overview:
The internship project revolves around the development of a chatbot tailored for Pizza Hut, aimed at enhancing customer interactions and streamlining the order placement process.

Purpose:
The primary objective of the chatbot is to provide Pizza Hut customers with a user-friendly platform to browse the menu, place orders, and receive assistance, ultimately improving the overall customer experience.


IMPLEMENTATION

Technical Details:
Language & Libraries: Python is chosen as the programming language, with the random library utilized for specific functionalities.
Approach: Employing a rules-based methodology, the chatbot generates responses by matching user inputs against predefined rules stored in a dictionary.

Functionalities:

User Input Processing: User inputs undergo standardization to lowercase to ensure uniform processing.

Response Generation: Responses are dynamically generated based on the matched rule or default response if no match is found.

Order Tracking: Boolean flags (ordering and address_needed) facilitate the management of the ordering workflow and address collection.


CODE EXPLAINATION

Structure:

Main Function: The main() function orchestrates user interactions and controls the conversation flow.

Response Generation: The generate_response() function crafts responses based on user input, employing rule-based matching and fallback mechanisms.

Response Generation:

Rule-Based Matching: User inputs are compared against predefined rules in the responses dictionary to determine the appropriate response.

Fallback Mechanism: A default response is provided when no specific rule matches the user input, ensuring a seamless conversational experience.


USAGE

Interaction:

Initiating Chat: Users are greeted with a welcoming message upon starting the conversation, prompting them to initiate interaction.

Order Placement: Keywords like "order" or "menu" trigger the ordering process, allowing users to navigate the menu and select items.

Address Provision: Users are prompted to provide their delivery address as necessary during the ordering process to finalize the order.

Ending Interaction: The conversation can be concluded by typing "bye," signaling the end of the session and thanking the user for their engagement.

Examples:

Placing an Order: Users can type "order" to commence the ordering process, followed by selecting items from the menu and providing necessary details.

Providing Address: When prompted, users can input their delivery address to finalize the order, ensuring accurate and timely delivery.


CONCLUSION

Project Overview: The internship project aimed to develop a chatbot for Pizza Hut, focusing on improving customer interactions and order placements.

Experience Reflection: The journey provided valuable insights into chatbot development, encompassing challenges tackled and lessons learned, contributing to personal and professional growth.

Future Prospects: Opportunities for future enhancements and feature enrichments were identified, paving the way for continued evolution and refinement of the chatbot to better serve Pizza Hut customers.


OUTPUT

![image](https://github.com/BingiSathwika/codetech/assets/142502651/1b905060-279f-44cd-9d0e-7f5adb9e8b9e)
 
# TASK 2
TITLE: CodTech IT Solutions Internship - Task Documentation: “TIC-TAC-TOE AI” Using PYTHON.

INTERN INFORMATION: 

Name: Bingi Sathwika

ID: C0D5077

INTRODUCTION

Overview:

Tic Tac Toe is a classic two-player game where each player takes turns marking spaces on a 3x3 grid. The objective is to form a horizontal, vertical, or diagonal line of three of your own symbols (X or O) before your opponent does. In this project, we aim to recreate this timeless game in Python, enhancing it with an AI opponent that utilizes the Minimax algorithm with Alpha-Beta pruning for strategic decision-making.

Purpose:

The purpose of developing this Tic Tac Toe game with an AI opponent is twofold. Firstly, it serves as an engaging and entertaining activity for users to enjoy, whether they're playing against the AI or challenging their friends. Secondly, it provides an opportunity to explore and implement fundamental concepts in artificial intelligence, such as search algorithms and decision-making strategies, within the context of a familiar and accessible game environment.


IMPLEMENTATION

Constants:

The constants X, O, and EMPTY are defined to represent the symbols used in the game (X and O) and empty spaces on the game board.

The game board is represented as a 1D list of length 9, with each element corresponding to a square on the 3x3 grid.

Board Initialization:

The create_board() function initializes the game board by creating a list of empty spaces using the EMPTY constant.

Displaying the Board:

The display_board() function prints the current state of the game board in a visually appealing format, allowing players to easily visualize the positions of their moves.


CODE EXPLAINATION

Winning Conditions:

The is_winner() function checks for winning configurations on the game board by iterating through a predefined set of winning combinations (rows, columns, and diagonals).

If any of these combinations contain three consecutive symbols belonging to the same player (X or O), the function returns True, indicating that the player has won the game.

AI Implementation:

The AI opponent is implemented using the Minimax algorithm with Alpha-Beta pruning, a common technique in game theory for determining the optimal move in a game.

The minimax() function recursively evaluates potential moves and assigns a score to each move based on the outcome of the game.

Alpha-Beta pruning is used to optimize the search process by eliminating branches that are guaranteed to be suboptimal, reducing the computational overhead of the algorithm.


USAGE

Player Interaction:

Players interact with the game by making moves on the game board. Human players input their moves using the human_move() function, while the AI opponent's moves are determined by the get_ai_move() function.

The game alternates between player turns, with each player attempting to outmaneuver their opponent by strategically placing their symbols on the board.

Main Game Loop:

The main game loop manages the flow of the game, iterating through player turns until a winner is determined or the game ends in a draw.

After each move, the game checks for win conditions or a full board to determine the outcome of the game.


CONCLUSION

Summary:

The Tic Tac Toe game with an AI opponent provides a fun and challenging experience for players of all skill levels, showcasing the application of algorithmic concepts in game development.

By implementing the Minimax algorithm with Alpha-Beta pruning, we've created an AI opponent capable of making intelligent and strategic moves, providing a formidable challenge for human players.

Future Enhancements:

While the current implementation offers a solid foundation for a Tic Tac Toe game with AI, there are several opportunities for further enhancements.

These may include implementing different difficulty levels for the AI, adding graphical user interface (GUI) elements to enhance the user experience, and integrating multiplayer functionality to allow players to compete against each other online.


OUTPUT	

![image](https://github.com/BingiSathwika/codetech/assets/142502651/6aeadf67-3484-4a4f-be19-50a354a22af3)
![image](https://github.com/BingiSathwika/codetech/assets/142502651/faa76f85-9635-41dc-98e7-023db9f80146)
![image](https://github.com/BingiSathwika/codetech/assets/142502651/c9846b06-754a-44b1-8c17-eaf15ea3c7a6)
![image](https://github.com/BingiSathwika/codetech/assets/142502651/6cc0d6e3-1ab7-428b-b358-1468cc7f3622)

 
