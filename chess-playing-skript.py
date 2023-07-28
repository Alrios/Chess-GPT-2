from transformers import GPT2LMHeadModel, GPT2Tokenizer
import chess

def init_board():
    board=chess.Board()
    return board

def update_board(board: chess.Board, san):
    try:
        board.push_san(san)
    except TypeError as e:
        print("I cannot think of any legal moves. I gave up.")
        exit(0)
    return board

def checkValidity(san, board):
    isLegal = True
    try:
        board.parse_san(san)
    except chess.IllegalMoveError as e:
        isLegal = False
    except chess.InvalidMoveError as e:
        isLegal = False
    except chess.AmbiguousMoveError as e:
        isLegal = False
    finally:
        return isLegal

def getOpponentMove(board):
    while True:
        try:
            move = str(input("\nTell me your move: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        legal = checkValidity(move, board)
        if not legal:
            print("\nSorry, your next move needs to be legal")
            continue
        else:
            break
    return move

def getMoveFromModel(model: GPT2LMHeadModel, tokenizer: GPT2Tokenizer, sentence, board):
    next_legal_move = None
    model_inputs = tokenizer(sentence, is_split_into_words=True,  truncation=True, padding=True, return_tensors="pt")

    beam_outputs = model.generate(
        model_inputs['input_ids'], 
        attention_mask=model_inputs["attention_mask"],     
        pad_token_id=tokenizer.pad_token_id, 
        max_new_tokens = 1,
        num_beams=20, 
        no_repeat_ngram_size=2, 
        num_return_sequences=20, 
        early_stopping=True
        )

    for output in beam_outputs:
        next_move = tokenizer.batch_decode(output, skip_special_tokens=True)[-1]
        if checkValidity(next_move, board):
            print(f"\n I will play {next_move}")
            next_legal_move = next_move
            break
    return next_legal_move


def main():
    
    print("Preparing the language Model...")
    
    # Load Model and Tokenizer
    model = GPT2LMHeadModel.from_pretrained('./chess-models/gtp2-300k')
    tokenizer = GPT2Tokenizer.from_pretrained('./chess-models/tokenizer/')
    
    board = init_board()
    sentence = []
    model_is_next = False


    while not board.is_checkmate():
        move = None
        print("\n")
        print(board)
        print("\n")

        if not model_is_next:
            move = getOpponentMove(board)
            model_is_next = True
        else:
            move = getMoveFromModel(model, tokenizer, sentence, board)
            model_is_next = False
        sentence.append(move)
        board = update_board(board, move)
        


if __name__ == "__main__":
    main()
