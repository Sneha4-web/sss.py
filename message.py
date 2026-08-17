import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="A Little Universe For You ❤️",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# PERSONALIZE THESE
# ============================================================

HIS_NAME = "Shamsher ji💕"
YOUR_NAME = "Sneha"

# Change these to your own memories
MEMORY_1 = """
When i first time liked your instagram posts
and then you message me for the first time💗
"""

MEMORY_2 = """
Our first meet :17 MAY,2021🤗
"""

MEMORY_3 = """
ek memory tuc dsoge tuhadi favourite one aa jo
"""

# Your personal emotional message
LOVE_MESSAGE = """
I don't know if I'll ever be able to put into words what
you mean to me.

Somehow, you became one of the most beautiful parts of my
life without me even realizing when it happened.

Thank you for being there, for making me smile, for listening
to me, for understanding the little things, and for simply
being YOU.

If I could choose one person to keep making memories with,
laughing with, annoying, loving, and growing with...

I'd choose you.

Every. Single. Time. ❤️
"""

# ============================================================
# CUSTOM CSS + HTML + JAVASCRIPT
# ============================================================

html_code = f"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width,
               initial-scale=1.0">

<title>A Little Universe For You ❤️</title>


<style>

@import url(
'https://fonts.googleapis.com/css2?family=Caveat:wght@500;600;700&family=Great+Vibes&family=Poppins:wght@300;400;500;600&display=swap'
);


/* =========================================================
   GLOBAL
   ========================================================= */

* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}

html,
body {{
    width: 100%;
    height: 100%;
    overflow: hidden;
}}

body {{

    font-family: Poppins, sans-serif;

    background:
        radial-gradient(
            circle at 20% 20%,
            rgba(255,120,180,.15),
            transparent 30%
        ),

        radial-gradient(
            circle at 80% 80%,
            rgba(160,100,255,.15),
            transparent 30%
        ),

        linear-gradient(
            145deg,
            #160c1e,
            #09070e
        );

    color: white;

}}


/* =========================================================
   BACKGROUND
   ========================================================= */

.background {{

    position: fixed;

    inset: 0;

    overflow: hidden;

    pointer-events: none;

}}

.star {{

    position: absolute;

    width: 3px;
    height: 3px;

    border-radius: 50%;

    background: white;

    opacity: .5;

    animation:
        twinkle
        2.5s
        infinite
        ease-in-out;

}}

@keyframes twinkle {{

    50% {{
        opacity: .1;
        transform: scale(.4);
    }}

}}


.floating-heart {{

    position: absolute;

    font-size: 18px;

    opacity: .15;

    animation:
        floatUp
        linear
        infinite;

}}

@keyframes floatUp {{

    from {{

        transform:
            translateY(110vh)
            rotate(0deg);

        opacity: 0;

    }}

    15% {{
        opacity: .18;
    }}

    to {{

        transform:
            translateY(-15vh)
            rotate(25deg);

        opacity: 0;

    }}

}}


/* =========================================================
   SCREENS
   ========================================================= */

.screen {{

    position: fixed;

    inset: 0;

    display: flex;

    align-items: center;

    justify-content: center;

    padding: 25px;

    opacity: 0;

    visibility: hidden;

    transform: scale(1.03);

    transition:
        opacity .8s ease,
        transform .8s ease,
        visibility .8s;

    overflow-y: auto;

}}

.screen.active {{

    opacity: 1;

    visibility: visible;

    transform: scale(1);

}}


.content {{

    position: relative;

    z-index: 5;

    width: 100%;

    max-width: 850px;

    text-align: center;

}}


/* =========================================================
   TEXT
   ========================================================= */

.kicker {{

    font-size: .75rem;

    letter-spacing: 4px;

    text-transform: uppercase;

    color: #f5b8d5;

    margin-bottom: 18px;

}}

h1 {{

    font-family:
        'Great Vibes',
        cursive;

    font-size:
        clamp(3.5rem, 10vw, 7rem);

    font-weight: 400;

    line-height: 1.05;

}}

.subtitle {{

    color: #d8cbd8;

    font-size:
        clamp(.9rem, 2.5vw, 1.1rem);

    line-height: 1.8;

    max-width: 600px;

    margin:
        15px auto 35px;

}}


/* =========================================================
   BUTTONS
   ========================================================= */

button {{

    border: none;

    cursor: pointer;

    font-family: Poppins, sans-serif;

    color: white;

    background:
        linear-gradient(
            135deg,
            #e75b9c,
            #a96be9
        );

    padding:
        15px 28px;

    border-radius: 999px;

    font-size: .95rem;

    box-shadow:
        0 12px 35px
        rgba(225,91,156,.25);

    transition:
        transform .2s,
        box-shadow .2s;

}}

button:hover {{

    transform:
        translateY(-3px);

    box-shadow:
        0 16px 40px
        rgba(225,91,156,.4);

}}

button:active {{

    transform:
        scale(.96);

}}


/* =========================================================
   HEART
   ========================================================= */

.heart-container {{

    height: 330px;

    display: flex;

    align-items: center;

    justify-content: center;

    position: relative;

}}

.big-heart {{

    width: 155px;

    height: 155px;

    background: #f05a9b;

    position: relative;

    transform: rotate(-45deg);

    animation:
        heartbeat
        1.2s
        infinite;

    filter:
        drop-shadow(
            0 0 28px
            rgba(255,78,157,.55)
        );

}}

.big-heart::before,
.big-heart::after {{

    content: "";

    position: absolute;

    width: 155px;

    height: 155px;

    border-radius: 50%;

    background: #f05a9b;

}}

.big-heart::before {{

    top: -77px;
    left: 0;

}}

.big-heart::after {{

    left: 77px;
    top: 0;

}}

.heart-text {{

    position: absolute;

    z-index: 10;

    font-family:
        'Great Vibes',
        cursive;

    font-size:
        clamp(2rem, 7vw, 4rem);

    line-height: 1.1;

    width: 320px;

    animation:
        heartText
        1.2s
        infinite;

}}

@keyframes heartbeat {{

    0%,
    100% {{
        transform:
            rotate(-45deg)
            scale(1);
    }}

    14% {{
        transform:
            rotate(-45deg)
            scale(1.12);
    }}

    28% {{
        transform:
            rotate(-45deg)
            scale(1);
    }}

    42% {{
        transform:
            rotate(-45deg)
            scale(1.08);
    }}

}}

@keyframes heartText {{

    0%,
    100% {{
        transform: scale(1);
    }}

    14% {{
        transform: scale(1.08);
    }}

    28% {{
        transform: scale(1);
    }}

    42% {{
        transform: scale(1.05);
    }}

}}


/* =========================================================
   GLASS CARD
   ========================================================= */

.card {{

    background:
        rgba(255,255,255,.065);

    border:
        1px solid
        rgba(255,255,255,.12);

    backdrop-filter:
        blur(15px);

    border-radius: 28px;

    padding: 35px;

    box-shadow:
        0 25px 80px
        rgba(0,0,0,.3);

}}

.card h2 {{

    font-family:
        'Great Vibes',
        cursive;

    font-size: 3.5rem;

    font-weight: 400;

    color: #ffb3d2;

}}

.card p {{

    color: #ddd0dd;

    line-height: 2;

    font-size: .98rem;

    margin-top: 20px;

}}

.highlight {{

    color: #ffb0cf;

}}


/* =========================================================
   KITTY
   ========================================================= */

.kitty {{

    font-size: 110px;

    line-height: 1;

    display: inline-block;

    cursor: pointer;

    user-select: none;

    filter:
        drop-shadow(
            0 15px 18px
            rgba(0,0,0,.25)
        );

    animation:
        kittyFloat
        2s
        infinite
        ease-in-out;

}}

@keyframes kittyFloat {{

    50% {{
        transform:
            translateY(-12px)
            rotate(2deg);
    }}

}}

.tap-hint {{

    color: #f6accb;

    margin:
        18px 0 28px;

    font-size: .9rem;

    letter-spacing: 1px;

}}

.message {{

    opacity: 0;

    transform:
        translateY(20px);

    transition: .8s;

}}

.message.show {{

    opacity: 1;

    transform:
        translateY(0);

}}

.message p {{

    font-family:
        Caveat,
        cursive;

    font-size:
        1.55rem;

    line-height: 1.55;

    color: #f5eaf2;

}}


/* =========================================================
   MEMORIES
   ========================================================= */

.memory-grid {{

    display: grid;

    grid-template-columns:
        repeat(3,1fr);

    gap: 14px;

    margin-top: 25px;

}}

.memory {{

    min-height: 140px;

    padding: 18px;

    border-radius: 20px;

    background:
        rgba(255,255,255,.06);

    border:
        1px solid
        rgba(255,255,255,.1);

    color: #f4d9e6;

    cursor: pointer;

    transition: .3s;

}}

.memory:hover {{

    transform:
        translateY(-5px);

    background:
        rgba(255,255,255,.1);

}}

.memory-icon {{

    display: block;

    font-size: 2rem;

    margin-bottom: 8px;

}}

.memory-text {{

    display: none;

    color: #e6d9e5;

    line-height: 1.6;

    font-size: .82rem;

}}

.memory.open
.memory-title {{

    display: none;

}}

.memory.open
.memory-text {{

    display: block;

}}


/* =========================================================
   GAME
   ========================================================= */

.game-area {{

    position: relative;

    height: 280px;

    margin: 10px 0;

}}

.hidden-heart {{

    position: absolute;

    font-size: 30px;

    cursor: pointer;

    transition:
        transform .2s;

    user-select: none;

}}

.hidden-heart:hover {{

    transform:
        scale(1.35);

}}

.game-status {{

    color: #cdbdca;

    font-size: .9rem;

    margin-bottom: 10px;

}}


/* =========================================================
   FINAL
   ========================================================= */

.final-heart {{

    font-size: 80px;

    animation:
        finalFloat
        2s
        infinite
        ease-in-out;

    filter:
        drop-shadow(
            0 0 25px
            rgba(255,100,170,.5)
        );

}}

@keyframes finalFloat {{

    50% {{
        transform:
            translateY(-10px)
            scale(1.05);
    }}

}}

.final-text {{

    font-family:
        Caveat,
        cursive;

    font-size:
        clamp(1.4rem,4vw,2rem);

    line-height: 1.6;

    color: #f4e5ee;

    margin:
        15px auto 25px;

}}

.signature {{

    font-family:
        'Great Vibes',
        cursive;

    font-size: 2.8rem;

    color: #ffb3d2;

}}


/* =========================================================
   HEART EXPLOSION
   ========================================================= */

.confetti {{

    position: fixed;

    z-index: 100;

    pointer-events: none;

    font-size: 20px;

    animation:
        confettiFall
        1.8s
        forwards
        ease-out;

}}

@keyframes confettiFall {{

    to {{

        transform:
            translate(
                var(--x),
                var(--y)
            )
            rotate(540deg);

        opacity: 0;

    }}

}}


/* =========================================================
   RESPONSIVE
   ========================================================= */

@media(max-width:650px) {{

    .screen {{
        padding: 18px;
    }}

    .card {{
        padding:
            25px 19px;
    }}

    .memory-grid {{
        grid-template-columns: 1fr;
    }}

    .memory {{
        min-height: 100px;
    }}

    .game-area {{
        height: 240px;
    }}

}}

</style>

</head>


<body>


<!-- =======================================================
     BACKGROUND
     ======================================================= -->

<div class="background">

    <div id="stars"></div>

    <div id="floatingHearts"></div>

</div>


<!-- =======================================================
     SCREEN 1
     ======================================================= -->

<section
    class="screen active"
    id="screen1"
>

<div class="content">

    <div class="kicker">
        A tiny surprise made with love
    </div>

    <h1>
        Click here, baby ❤️
    </h1>

    <p class="subtitle">

        I made a little something for you.

        <br>

        Take your time…

        there are a few surprises
        waiting inside.

    </p>

    <button onclick="showScreen(2)">

        Open my heart ✨

    </button>

    <div
        style="
        margin-top:16px;
        color:#a998a9;
        font-size:.75rem;
        "
    >

        P.S. Don't rush.
        I want you to feel every little part. ♡

    </div>

</div>

</section>


<!-- =======================================================
     SCREEN 2
     ======================================================= -->

<section
    class="screen"
    id="screen2"
>

<div class="content">

    <div class="kicker">
        First things first…
    </div>


    <div class="heart-container">

        <div class="big-heart"></div>

        <div class="heart-text">

            I love you,

            <br>

            {HIS_NAME}❤️

        </div>

    </div>


    <p class="subtitle">

        More than this little heart
        could ever hold.

    </p>


    <button onclick="showScreen(3)">

        There's more… 💕

    </button>

</div>

</section>


<!-- =======================================================
     SCREEN 3
     ======================================================= -->

<section
    class="screen"
    id="screen3"
>

<div class="content">

    <div class="kicker">

        Billi ne kehna tuhanu kuj

    </div>


    <div
        class="kitty"
        id="kitty"
    >

        🐱

    </div>


    <div class="tap-hint">

        ♡ DOUBLE TAP ME, BABY ♡

    </div>


    <div
        class="message"
        id="loveMessage"
    >

        <div class="card">

            <h2>
                For you…
            </h2>


            <p>

                {LOVE_MESSAGE}

            </p>


            <button
                style="margin-top:28px;"
                onclick="showScreen(4)"
            >

                Remember this? 🌷

            </button>

        </div>

    </div>

</div>

</section>


<!-- =======================================================
     SCREEN 4
     ======================================================= -->

<section
    class="screen"
    id="screen4"
>

<div class="content">

    <div class="kicker">

        Our little universe

    </div>


    <div class="card">

        <h2>
            Do you remember? 🥺
        </h2>


        <p>

            Tap each little memory.

            <br>

            These are the little pieces
            of our story that I never want
            to forget.

        </p>


        <div class="memory-grid">


            <!-- MEMORY 1 -->

            <div
                class="memory"
                onclick="toggleMemory(this)"
            >

                <span class="memory-icon">
                    💭
                </span>

                <div class="memory-title">

                    Our first conversation

                </div>

                <div class="memory-text">

                    {MEMORY_1}

                </div>

            </div>


            <!-- MEMORY 2 -->

            <div
                class="memory"
                onclick="toggleMemory(this)"
            >

                <span class="memory-icon">
                    🫶
                </span>

                <div class="memory-title">

                    My favorite memory

                </div>

                <div class="memory-text">

                    {MEMORY_2}

                </div>

            </div>


            <!-- MEMORY 3 -->

            <div
                class="memory"
                onclick="toggleMemory(this)"
            >

                <span class="memory-icon">
                    ❤️
                </span>

                <div class="memory-title">

                    The moment I knew

                </div>

                <div class="memory-text">

                    {MEMORY_3}

                </div>

            </div>


        </div>


        <button
            style="margin-top:25px;"
            onclick="showScreen(5)"
        >

            One last little game 👀

        </button>

    </div>

</div>

</section>


<!-- =======================================================
     SCREEN 5
     ======================================================= -->

<section
    class="screen"
    id="screen5"
>

<div class="content">

    <div class="kicker">

        Okay baby…

    </div>


    <div class="card">

        <h2>

            Find the hidden heart ❤️

        </h2>


        <p>

            There are lots of hearts around…

            <br>

            but only one opens
            the final surprise.

        </p>


        <div
            class="game-status"
            id="gameStatus"
        >

            Find it.
            I know you can. 👀

        </div>


        <div
            class="game-area"
            id="gameArea"
        >

        </div>

    </div>

</div>

</section>


<!-- =======================================================
     SCREEN 6
     ======================================================= -->

<section
    class="screen"
    id="screen6"
>

<div class="content">

    <div class="final-heart">
        ❤️
    </div>


    <div class="kicker">

        You found it.

    </div>


    <div class="card">

        <h2>

            And this is my favorite part…

        </h2>


        <div class="final-text">

            If you ever wonder
            how much I love you…

            <br>

            more than these words
            can explain.

            <br>

            more than this little website
            could ever show.

            <br><br>

            I'll keep choosing you —

            <br>

            <span class="highlight">

                today,
                tomorrow,
                and every day after that. ❤️

            </span>

        </div>


        <div class="signature">

            Made with love,
            just for you.

        </div>


        <p
            style="
            margin-top:10px;
            color:#bcaebb;
            "
        >

            — {YOUR_NAME} ♡

        </p>

    </div>

</div>

</section>


<script>


/* =========================================================
   CREATE STARS
   ========================================================= */

const stars =
document.getElementById("stars");


for(let i = 0; i < 90; i++){{

    const star =
    document.createElement("div");

    star.className =
    "star";

    star.style.left =
    Math.random() * 100 + "%";

    star.style.top =
    Math.random() * 100 + "%";

    star.style.animationDelay =
    Math.random() * 3 + "s";

    star.style.animationDuration =
    (1.5 + Math.random() * 3) + "s";

    stars.appendChild(star);

}}


/* =========================================================
   FLOATING HEARTS
   ========================================================= */

const floatingHearts =
document.getElementById(
    "floatingHearts"
);


for(let i = 0; i < 20; i++){{

    const heart =
    document.createElement("div");

    heart.className =
    "floating-heart";

    const symbols =
    ["♡","♥","✦","❤","💕"];

    heart.textContent =
    symbols[
        Math.floor(
            Math.random()
            * symbols.length
        )
    ];

    heart.style.left =
    Math.random() * 100 + "%";

    heart.style.animationDelay =
    (-Math.random() * 12) + "s";

    heart.style.animationDuration =
    (8 + Math.random() * 10) + "s";

    floatingHearts.appendChild(
        heart
    );

}}


/* =========================================================
   SCREEN NAVIGATION
   ========================================================= */

function showScreen(number){{

    document
    .querySelectorAll(".screen")
    .forEach(
        screen =>
        screen.classList.remove("active")
    );

    document
    .getElementById(
        "screen" + number
    )
    .classList.add("active");


    if(number === 5){{
        createGame();
    }}

}}


/* =========================================================
   KITTY DOUBLE TAP
   ========================================================= */

const kitty =
document.getElementById("kitty");

let lastTap = 0;


kitty.addEventListener(
    "click",
    function(){{

        const current =
        Date.now();


        if(
            current - lastTap
            < 450
        ){{

            kitty.style.transform =
            "scale(1.2) rotate(-8deg)";


            setTimeout(
                () =>
                kitty.style.transform = "",
                300
            );


            document
            .getElementById(
                "loveMessage"
            )
            .classList.add("show");


            heartExplosion(25);

        }}


        lastTap = current;

    }}
);


/* =========================================================
   MEMORY CARDS
   ========================================================= */

function toggleMemory(element){{

    element.classList.toggle(
        "open"
    );

}}


/* =========================================================
   HIDDEN HEART GAME
   ========================================================= */

function createGame(){{

    const area =
    document.getElementById(
        "gameArea"
    );

    area.innerHTML = "";


    const secret =
    Math.floor(
        Math.random() * 18
    );


    for(let i = 0; i < 18; i++){{

        const heart =
        document.createElement("div");


        heart.className =
        "hidden-heart";


        const symbols =
        [
            "♡",
            "💗",
            "💕",
            "♡",
            "💖"
        ];


        heart.textContent =
        symbols[
            Math.floor(
                Math.random()
                * symbols.length
            )
        ];


        heart.style.left =
        (5 + Math.random() * 85)
        + "%";


        heart.style.top =
        (5 + Math.random() * 80)
        + "%";


        heart.onclick =
        function(){{

            if(i === secret){{

                document
                .getElementById(
                    "gameStatus"
                )
                .textContent =
                "You found my heart. 🥹❤️";


                heartExplosion(55);


                setTimeout(
                    () => showScreen(6),
                    900
                );

            }}

            else{{

                heart.textContent =
                "♡";

                heart.style.opacity =
                ".3";


                document
                .getElementById(
                    "gameStatus"
                )
                .textContent =
                "Not this one… try again, baby. 😌";

            }}

        }};


        area.appendChild(
            heart
        );

    }}

}}


/* =========================================================
   HEART EXPLOSION
   ========================================================= */

function heartExplosion(
    count = 25
){{

    const symbols =
    [
        "❤️",
        "💕",
        "💗",
        "💖",
        "✨",
        "♡"
    ];


    for(
        let i = 0;
        i < count;
        i++
    ){{

        const element =
        document.createElement(
            "div"
        );


        element.className =
        "confetti";


        element.textContent =
        symbols[
            Math.floor(
                Math.random()
                * symbols.length
            )
        ];


        element.style.left =
        (45 + Math.random() * 10)
        + "vw";


        element.style.top =
        (45 + Math.random() * 10)
        + "vh";


        element.style.setProperty(
            "--x",
            (Math.random() * 400 - 200)
            + "px"
        );


        element.style.setProperty(
            "--y",
            (Math.random() * -450 - 80)
            + "px"
        );


        element.style.animationDelay =
        Math.random() * .25
        + "s";


        document.body.appendChild(
            element
        );


        setTimeout(
            () => element.remove(),
            2200
        );

    }}

}}


/* =========================================================
   CURSOR HEARTS
   ========================================================= */

let heartTimer = 0;


document.addEventListener(
    "mousemove",
    function(event){{

        if(
            Date.now() - heartTimer
            > 180
        ){{

            const heart =
            document.createElement(
                "div"
            );


            heart.textContent = "♡";


            heart.style.position =
            "fixed";

            heart.style.left =
            event.clientX + "px";

            heart.style.top =
            event.clientY + "px";

            heart.style.pointerEvents =
            "none";

            heart.style.zIndex =
            "1000";

            heart.style.color =
            "#ff9fc8";

            heart.style.fontSize =
            "14px";

            heart.style.transition =
            "all .9s ease";


            document.body.appendChild(
                heart
            );


            setTimeout(() => {{

                heart.style.transform =
                "translateY(-30px) scale(.2)";

                heart.style.opacity = "0";

            }}, 20);


            setTimeout(
                () => heart.remove(),
                900
            );


            heartTimer =
            Date.now();

        }}

    }}

);


</script>

</body>

</html>
"""


# ============================================================
# DISPLAY THE WEBSITE INSIDE STREAMLIT
# ============================================================

components.html(
    html_code,
    height=1000,
    scrolling=False
) 
