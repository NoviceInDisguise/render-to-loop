# Render To Loop
A project to make a simple, automated method of rendering simple backgrounds and particle effects into a seamless loop.

# Basic Crossfade
This method cuts the selected sequence in half, and translates it up one channel. The result is a top channel which has a start-frame that comes directly after the bottom channel's end-frame. A simple set of alpha keyframes results in a nice crossfade. The main weakness of this method is that the resulting loop is only half as long as the source sequence.

# Complex Crossfade [unfinished]
This method duplicates the selected sequence, cuts it in half, and switches the position of the halves. The alpha is then keyframed and a full-length crossfade effect is achieved.
