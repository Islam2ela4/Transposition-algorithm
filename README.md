Rail Fence cipher
The Rail Fence cipher is a form of transposition cipher that gets its name from the way in which it is encoded. In the rail fence cipher, the plaintext is written downwards on successive "rails" of an imaginary fence, then moving up when we get to the bottom. The message is then read off in rows. For example, using three "rails" and a message of 'WE ARE DISCOVERED. FLEE AT ONCE', the cipherer writes out:

W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . A . . . I . . . V . . . D . . . E . . . N . .
Then reads off:

WECRL TEERD SOEEF EAOCA IVDEN
(The ciphrer has broken this ciphertext up into blocks of five to help avoid errors. This is a common technique used to make the cipher more easily readable. The spacing is not related to spaces in the plaintext and so does not carry any information about the plaintext.)

The rail fence cipher was used by the ancient Greeks in the scytale, a mechanical system of producing a transposition cipher. The system consisted of a cylinder and a ribbon that was wrapped around the cylinder. The message to be encrypted was written on the coiled ribbon. The letters of the original message would be rearranged when the ribbon was uncoiled from the cylinder. However, the message was easily decrypted when the ribbon was recoiled on a cylinder of the same diameter as the encrypting cylinder.[1]

Route cipher
In a route cipher, the plaintext is first written out in a grid of given dimensions, then read off in a pattern given in the key. For example, using the same plaintext that we used for rail fence:

W R I O R F E O E 
E E S V E L A N J 
A D C E D E T C X 
The key might specify "spiral inwards, clockwise, starting from the top right". That would give a cipher text of:

EJXCTEDECDAEWRIORFEONALEVSE
Route ciphers have many more keys than a rail fence. In fact, for messages of reasonable length, the number of possible keys is potentially too great to be enumerated even by modern machinery. However, not all keys are equally good. Badly chosen routes will leave excessive chunks of plaintext, or text simply reversed, and this will give cryptanalysts a clue as to the routes.

A variation of the route cipher was the Union Route Cipher, used by Union forces during the American Civil War. This worked much like an ordinary route cipher, but transposed whole words instead of individual letters. Because this would leave certain highly sensitive words exposed, such words would first be concealed by code. The cipher clerk may also add entire null words, which were often chosen to make the ciphertext humorous.[citation needed]

Columnar transposition
In a columnar transposition, the message is written out in rows of a fixed length, and then read out again column by column, and the columns are chosen in some scrambled order. Both the width of the rows and the permutation of the columns are usually defined by a keyword. For example, the keyword ZEBRAS is of length 6 (so the rows are of length 6), and the permutation is defined by the alphabetical order of the letters in the keyword. In this case, the order would be "6 3 2 4 1 5".

In a regular columnar transposition cipher, any spare spaces are filled with nulls; in an irregular columnar transposition cipher, the spaces are left blank. Finally, the message is read off in columns, in the order specified by the keyword. For example, suppose we use the keyword ZEBRAS and the message WE ARE DISCOVERED. FLEE AT ONCE. In a regular columnar transposition, we write this into the grid as follows:

6 3 2 4 1 5
W E A R E D
I S C O V E 
R E D F L E 
E A T O N C 
E Q K J E U 
providing five nulls (QKJEU), these letters can be randomly selected as they just fill out the incomplete columns and are not part of the message. The ciphertext is then read off as:

EVLNE ACDTK ESEAQ ROFOJ DEECU WIREE
In the irregular case, the columns are not completed by nulls:

6 3 2 4 1 5
W E A R E D 
I S C O V E 
R E D F L E 
E A T O N C 
E 
This results in the following ciphertext:

EVLNA CDTES EAROF ODEEC WIREE
To decipher it, the recipient has to work out the column lengths by dividing the message length by the key length. Then he can write the message out in columns again, then re-order the columns by reforming the key word.

In a variation, the message is blocked into segments that are the key length long and to each segment the same permutation (given by the key) is applied. This is equivalent to a columnar transposition where the read-out is by rows instead of columns.

Columnar transposition continued to be used for serious purposes as a component of more complex ciphers at least into the 1950s.

Double transposition
A single columnar transposition could be attacked by guessing possible column lengths, writing the message out in its columns (but in the wrong order, as the key is not yet known), and then looking for possible anagrams. Thus to make it stronger, a double transposition was often used. This is simply a columnar transposition applied twice. The same key can be used for both transpositions, or two different keys can be used.

As an example, we can take the result of the irregular columnar transposition in the previous section, and perform a second encryption with a different keyword, STRIPE, which gives the permutation "564231":

5 6 4 2 3 1 
E V L N A C
D T E S E A
R O F O D E
E C W I R E
E
As before, this is read off columnwise to give the ciphertext:

CAEEN SOIAE DRLEF WEDRE EVTOC
If multiple messages of exactly the same length are encrypted using the same keys, they can be anagrammed simultaneously. This can lead to both recovery of the messages, and to recovery of the keys (so that every other message sent with those keys can be read).

During World War I, the German military used a double columnar transposition cipher, changing the keys infrequently. The system was regularly solved by the French, naming it Übchi, who were typically able to quickly find the keys once they'd intercepted a number of messages of the same length, which generally took only a few days. However, the French success became widely known and, after a publication in Le Matin, the Germans changed to a new system on 18 November 1914.[2]

During World War II, the double transposition cipher was used by Dutch Resistance groups, the French Maquis and the British Special Operations Executive (SOE), which was in charge of managing underground activities in Europe.[3] It was also used by agents of the American Office of Strategic Services[4] and as an emergency cipher for the German Army and Navy.

Until the invention of the VIC cipher, double transposition was generally regarded as the most complicated cipher that an agent could operate reliably under difficult field conditions.

Cryptanalysis
The double transposition cipher can be treated as a single transposition with a key as long as the product of the lengths of the two keys.[5]

In late 2013, a double transposition challenge, regarded by its author as undecipherable, was solved by George Lasry using a divide-and-conquer approach where each transposition was attacked individually.[6]

Myszkowski transposition
A variant form of columnar transposition, proposed by Émile Victor Théodore Myszkowski in 1902, requires a keyword with recurrent letters. In usual practice, subsequent occurrences of a keyword letter are treated as if the next letter in alphabetical order, e.g., the keyword TOMATO yields a numeric keystring of "532164."

In Myszkowski transposition, recurrent keyword letters are numbered identically, TOMATO yielding a keystring of "432143."

4 3 2 1 4 3
W E A R E D
I S C O V E
R E D F L E
E A T O N C
E
Plaintext columns with unique numbers are transcribed downward; those with recurring numbers are transcribed left to right:

ROFOA CDTED SEEEA CWEIV RLENE
