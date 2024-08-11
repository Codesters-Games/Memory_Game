# choosing the sprites od the cards
deck = ["alien1", "athlete1", "bike", "chameleon1", "present2", "recyclingbin", "pinetree7", "candy"]

# Variables to store the indices of the first and second cards clicked by the user
first_clicked_card_index= -1
second_clicked_card_index= -1

# Variables to store the sprites of the first and second cards clicked by the user
first_clicked_card_sprite= -1
second_clicked_card_sprite= -1

# Duplicate the deck to have two of each sprite for the memory game
deck = deck * 2

# Function to shuffle the deck of cards
def shuffle_cards():
    for i, card in enumerate(deck):
        if (i==len(deck)-1): 
            break
        # get a random card index to swap with the current card
        random_index = random.randint(i+1, len(deck)-1 )
        # swap the current with the random one
        deck[i] = deck[random_index]
        deck[random_index] = card
        
# function to create cards
def create_card():
    # loop to create many cards
    for i in range(4):
        for j in range(4):
            card = codesters.Rectangle(-185 + (j*120), 145-(i*110), 80, 100, "DeepSkyBlue")
            # sprite = codesters.Quad(-240 + (j*120), 145-(i*110), -185 + (j*120), + 80 + 145-(i*110), 150 -240 + (j*120), + 80 + 145-(i*110), -150 + (j*120), 145-(i*110), "blue")
            # Assign an ID to each card based on its position/index in the grid
            card.id = j +(i*4)
            # Set an event listener for when the card is clicked
            card.event_click(card_click_event)
            
        
# Function to handle the logic when a card is clicked
def card_click_event(card):
    global first_clicked_card_index, second_clicked_card_index, first_clicked_card_sprite, second_clicked_card_sprite
    # Check if this is the first card clicked by the user
    if first_clicked_card_index == -1:
        first_clicked_card_index = card.id
        # Display the image corresponding to the card from the deck
        first_clicked_card_sprite = codesters.Sprite(deck[first_clicked_card_index], card.get_x(), card.get_y())
        first_clicked_card_sprite.set_size(.25)
    
    elif second_clicked_card_index == -1 and card.id != first_clicked_card_index:
        second_clicked_card_index = card.id
        # Display the image corresponding to the card from the deck
        second_clicked_card_sprite = codesters.Sprite(deck[second_clicked_card_index], card.get_x(), card.get_y())
        second_clicked_card_sprite.set_size(.25)
        # Wait for 2 seconds to let the user see the second card
        stage.wait(2)
        
        # check if the two do not match
        if deck[first_clicked_card_index] is not deck[second_clicked_card_index]:
            # If they don't match, remove the images and show the placeholders again
            stage.remove_sprite(first_clicked_card_sprite)
            stage.remove_sprite(second_clicked_card_sprite)
     
        # Reset the first and second card variables to their initial values
        first_clicked_card_index= -1
        second_clicked_card_index= -1
       

    print("f", first_clicked_card_index)
    print("s", second_clicked_card_index)


# shuffle dards first
shuffle_cards()
# then create the grid
create_card()

