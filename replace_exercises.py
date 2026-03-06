#!/usr/bin/env python3
"""Replace EXERCISES block in index.html with the full 120-exercise library."""

import re

# All 120 exercises: (name, description) per group
CHEST = [
    ("Barbell Bench Press", "Lie on a flat bench, grasp the bar slightly wider than shoulder-width, lower it to touch the chest, and press upward to extend the elbows."),
    ("Pec Deck Machine", "Sit at the machine and bring your hands or arms together in an arc motion to squeeze the chest."),
    ("Bent-Forward Cable Crossover", "Stand in a staggered stance, bend forward, and bring cable handles together in a wide arc."),
    ("Seated Chest Press Machine", "Sit on the machine and press the handles forward to engage the chest."),
    ("Incline Dumbbell Press", "Set a bench to a 15- to 45-degree angle, lower dumbbells to chest level, and press them up."),
    ("Dumbbell Flys", "Lie flat, keep a slight bend in the elbows, lower weights laterally until the chest stretches, and raise them back up."),
    ("Parallel Bar Dips", "Suspend your body on dip bars, lean slightly forward, and lower yourself until the elbows form a 90-degree angle."),
    ("Suspended Push-Ups", "Perform push-ups using suspension straps to rely on bodyweight and force stabilization."),
    ("Stability Ball Push-Ups", "Execute a push-up with your hands or feet resting on a stability ball for added core engagement."),
    ("Standard Push-Ups", "Place hands flat on the floor, keep the body straight, lower the chest near the floor, and push back up."),
    ("Flat Dumbbell Press", "Lie on a flat bench, lower dumbbells to the sides of your chest, and push them upward."),
    ("Cable Fly", "Stand between cable pulleys set at shoulder height and connect your arms in front of you while keeping them straight."),
    ("Dumbbell Pullover", "Lie on a bench, hold a dumbbell over your chest, and lower it backward over your head with a slight elbow bend."),
    ("15-Degree Decline Dumbbell Press", "Set the bench to a slight decline and press dumbbells upward to target the lower chest."),
    ("Close-Grip Bench Press", "Perform a flat bench press using a grip slightly wider than shoulder-width and keeping elbows tucked."),
    ("Incline Bench Press", "Perform a barbell bench press on a 15- to 45-degree incline to emphasize the upper pectorals."),
    ("Decline Bench Press", "Perform a barbell bench press on a 15- to 30-degree decline to target the lower pectorals."),
    ("High Cable Fly", "Set cable pulleys to a high position and move arms downward to tap knuckles in front of the lower chest."),
    ("Banded Push-Up", "Perform a push-up with a resistance band stretched across the back to add resistance at the top."),
    ("Deficit Push-Up", "Elevate hands on boxes or plates to allow the chest to stretch deeper at the bottom of the movement."),
    ("Smith Machine Press", "Execute a bench press utilizing the guided barbell of a Smith machine for extra stability."),
    ("Incline Smith Machine Press", "Use the Smith machine on an incline bench to target the upper chest with added stability."),
    ("Seated Cable Pec Fly", "Sit on a bench between cable stacks and pull handles together for chest isolation."),
    ("Cable Press Around", "Press a single cable across your body's midline to get the pectoral muscle fully contracted."),
    ("Floor Press", "Lie flat on the floor and press weights upward until your elbows touch the floor, restricting the range of motion."),
    ("Guillotine Press", "Lower the barbell toward the neck to stretch the pecs, though this exercise carries a high risk of injury and is generally considered ineffective."),
    ("Hex Press", "Press dumbbells together while pressing them up, which offers minimal chest stretch and is considered a poor choice."),
    ("Plate Press", "Press a weight plate upward with both hands; this is awkward and offers low overload potential."),
    ("Crossbody Standing Dumbbell Fly", "Stand and sweep a dumbbell across your body, which provides zero tension during the stretch phase."),
    ("Dumbbell Chest Press", "A versatile press using dumbbells that allows you to adjust the elbow path for shoulder comfort."),
]

BACK = [
    ("Pull-Up", "Hang from a bar with an overhand grip wider than your shoulders and pull your body up."),
    ("Chin-Up", "Use an underhand, shoulder-width grip on a bar to pull yourself up, emphasizing the lats and biceps."),
    ("Band-Assisted Pull-Up", "Step into a resistance band looped around the bar to help pull you up from the bottom position."),
    ("Lat Pulldown", "Sit at a machine and pull a straight bar down to the upper chest with an overhand grip."),
    ("Barbell Row", "Hinge forward at the hips and pull a barbell to your upper abs or torso."),
    ("Pendlay Row", "Perform a barbell row starting from a dead stop on the floor for every repetition."),
    ("Single-Arm Dumbbell Row", "Support one knee and hand on a bench and row a dumbbell backward toward your hip."),
    ("Chest-Supported T-Bar Row", "Rest your chest against an angled pad and row horizontal handles upward."),
    ("Straight-Arm Lat Pullover", "Stand back from a high cable pulley and pull a bar or rope down with straight arms."),
    ("Cable Lat Pull-In", "Kneel perpendicular to a cable machine and drive your elbow inward toward your torso."),
    ("Inverted Row", "Hang under a secured bar or suspension straps and pull your chest upward."),
    ("Seated Cable Row", "Sit at a low pulley station and row the handle toward your stomach while keeping your back straight."),
    ("Landmine T-Bar Row", "Row the weighted end of a barbell anchored in a landmine using a V-handle."),
    ("Upright Row", "Pull a barbell or cable upward toward your chin, keeping the weight close to your body."),
    ("Wide Grip Lat Pulldown", "Perform a pulldown with a wide grip to provide a big stretch on the lats."),
    ("Neutral Grip Lat Pulldown", "Use parallel handles on a pulldown machine to keep elbows tucked."),
    ("Half-Kneeling One-Arm Lat Pulldown", "Perform a single-arm pulldown on one knee to maximize the stretch."),
    ("Cross Body Lat Pull Around", "Twist your torso 90 degrees and pull a single cable across your body."),
    ("Chest-Supported Row (Machine)", "Sit at a row machine with a chest pad to eliminate lower back fatigue."),
    ("Dumbbell Helms Row", "Brace your chest against the back of an incline bench and row dumbbells upward."),
    ("Seal Row", "Lie completely flat on an elevated bench and row a barbell upward."),
    ("Cable Lat Pullover (Lat Prayer)", "Bend forward using a rope attachment to deeply stretch the lats on the negative phase."),
    ("Renegade Row", "Row dumbbells while holding a plank position, though it lacks the stability needed to maximize muscle growth."),
    ("Croc Row", "Perform heavy, high-rep dumbbell rows using slight momentum."),
    ("Kelso Shrug", "Retract your shoulder blades from a chest-supported row position without bending your elbows."),
    ("EZ-Bar Chest-Supported Row", "Row an EZ-curl bar using an underhand grip while lying face down on a bench."),
    ("Seated One-Arm Chest-Supported Cable Row", "Sit upright at a machine to row one cable handle at a time."),
    ("Three-Point Dumbbell Row", "Use a staggered stance with one hand bracing on a bench while rowing a dumbbell."),
    ("Pronated Narrow-Grip Pulldown", "Perform a lat pulldown using a narrow overhand grip."),
    ("Reverse Grip Pulldown", "Pull a bar down using an underhand (supinated) grip."),
]

SHOULDERS = [
    ("Dumbbell Shoulder Press", "Press dumbbells upward from shoulder height while standing or seated."),
    ("45-Degree Incline Row", "Lie face down on an incline bench and row dumbbells high with flared elbows."),
    ("Seated Rear Lateral Raise", "Sit on a bench, bend your torso over, and raise dumbbells out to your sides."),
    ("Rear Delt Fly (Machine)", "Sit facing a pec deck machine and pull the handles backward."),
    ("Face Pulls", "Use a high cable pulley to pull a rope toward your forehead, flaring your elbows."),
    ("Barbell Overhead Press", "Press a barbell from the upper chest to full extension overhead."),
    ("Dumbbell Seated Shoulder Press", "Sit on a bench with back support and press dumbbells overhead."),
    ("Dumbbell Lateral Raise", "Raise dumbbells out to your sides until they reach shoulder height."),
    ("Cable Upright Row", "Pull a cable rope attachment upward toward your chin with elbows leading."),
    ("Dumbbell Bent-Over Reverse Fly", "Bend over with a flat back and lift dumbbells out to the sides."),
    ("Reverse Pec Deck", "Use the pec deck facing the pad to isolate the rear deltoids."),
    ("Band Pull-Aparts", "Hold a resistance band with straight arms and pull it apart to squeeze the rear delts."),
    ("Lean-In Dumbbell Lateral Raise", "Lean sideways against a rack or bench while raising a dumbbell to increase stretch tension."),
    ("Super ROM Lateral Raise", "Lift dumbbells all the way overhead for a full side delt contraction."),
    ("Machine Shoulder Press", "Perform vertical presses using a machine to safely push to failure."),
    ("Arnold-Style Side-Lying Dumbbell Raise", "Lie sideways on an incline bench and perform lateral raises to maximize tension."),
    ("Atlantis Standing Machine Lateral Raise", "Use a specialized standing machine that provides even resistance across the lateral raise."),
    ("Seated Machine Lateral Raise", "Sit in a machine with arm pads to raise the arms laterally."),
    ("Cable Lateral Raise", "Raise a single cable handle out to the side for constant tension."),
    ("Cable Y Raise", "Sweep two cables up, out, and backward simultaneously."),
    ("Behind the Back Cuffed Lateral Raise", "Attach cables to wrist cuffs behind your back and raise outward."),
    ("Banded Lateral Raise", "Perform lateral raises utilizing resistance bands."),
    ("Reverse Cable Crossover", "Cross your arms over to grasp opposing high cables and pull them outward."),
    ("Floor/Seated Face Pull", "Perform face pulls while sitting or lying down to eliminate balance requirements."),
    ("Prone Y-Raises", "Lie face down on a mat and lift your arms above your head in a Y shape."),
    ("Single-Arm Row with External Rotation", "Row a dumbbell and externally rotate the forearm at the top of the movement."),
    ("Cable Reverse Flys", "Cross cables over each other at chest height and pull arms back in a wide arc."),
    ("Dumbbell Front Raise", "Raise dumbbells straight forward, though this is often considered redundant for front delts."),
    ("Barbell Upright Row", "Pull a barbell upward to your chest to target side delts and upper traps."),
    ("Cable Diagonal Raise", "Pull a low cable handle diagonally across your body."),
]

ARMS = [
    ("Barbell Bicep Curl", "Stand holding a barbell with an underhand grip and curl the weight toward your shoulders."),
    ("Dumbbell Hammer Curl", "Hold dumbbells with a neutral grip and curl upward to target the brachialis."),
    ("Reverse Curl", "Curl a barbell or dumbbells using an overhand (pronated) grip to emphasize the forearms."),
    ("Cable Rope Hammer Curl", "Perform a hammer curl using a rope attachment on a low cable pulley."),
    ("Reverse-Grip EZ Bar Curl", "Use an EZ curl bar with an overhand grip to work the brachioradialis."),
    ("Hammer Concentration Curl", "Perform a concentration curl with a neutral grip while seated."),
    ("Swiss Bar Hammer Curl", "Curl using a multi-grip Swiss bar that allows for neutral hand placement."),
    ("Incline Hammer Curl", "Sit on an incline bench and perform hammer curls to stretch the biceps."),
    ("Cross-Body Hammer Curl", "Curl a dumbbell across your torso toward the opposite shoulder using a neutral grip."),
    ("Chest-Supported Hammer Curl", "Straddle an incline bench face down and perform neutral-grip curls."),
    ("Triceps Pushdown", "Attach a bar or rope to a high cable pulley and push down, extending your elbows fully."),
    ("Preacher Hammer Curl", "Rest your upper arms on a preacher pad and perform neutral-grip curls."),
    ("EZ-Bar Curl", "Curl an angled EZ-bar to reduce strain on the wrists."),
    ("Standing Dumbbell Curl", "Curl dumbbells simultaneously while standing."),
    ("Preacher Curl (Barbell/Dumbbell)", "Rest arms over an angled pad and curl upward to lock the elbows in place."),
    ("Incline Dumbbell Curl", "Sit on an incline bench, allowing your arms to hang back, and curl upward."),
    ("Lying Dumbbell Curl", "Lie flat on a bench, allowing the arms to hang fully to maximize bicep stretch."),
    ("Scott Curl", "Perform a preacher curl with a completely vertical arm pad."),
    ("Flat Bench Curl", "Lie face down or brace against a flat bench to curl with extreme stretch."),
    ("Machine Preacher Curl", "Use a loaded machine pad to perform strict preacher curls."),
    ("Waiter Curl", "Curl a weight plate holding its edges; noted as a poor exercise due to wrist strain."),
    ("Drag Curl", "Drag a barbell up your torso by pulling your elbows backward."),
    ("Spider Curl", "Lie face down on an incline bench with arms hanging straight down and curl upward."),
    ("21s (Biceps)", "Perform 7 bottom-half reps, 7 top-half reps, and 7 full reps in one set."),
    ("Face-Away Bayesian Cable Curl", "Stand facing away from a low pulley to stretch the biceps deeply behind you."),
    ("Cheat Curl", "Use slight body momentum to curl a heavier weight, then strictly control the negative phase."),
    ("Strict Curl", "Stand with back and head flat against a wall to prevent momentum while curling."),
    ("Inverse Zottman Curl", "Curl the weight up with a neutral grip and lower it with a supinated grip."),
    ("Overhead Triceps Extension", "Extend a cable or dumbbell overhead from behind your neck to stretch the triceps long head."),
    ("Skull Crusher", "Lie flat and lower an EZ-bar behind your head, then extend your elbows."),
]


def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def format_group(key, items):
    lines = [f"  {key}: ["]
    for name, desc in items:
        lines.append('    {')
        lines.append(f'      name: "{esc(name)}",')
        lines.append(f'      description: "{esc(desc)}"')
        lines.append('    },')
    lines.append("  ]")
    return "\n".join(lines)


def main():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    new_block = "const EXERCISES = {\n"
    new_block += format_group("chest", CHEST) + ",\n"
    new_block += format_group("back", BACK) + ",\n"
    new_block += format_group("shoulders", SHOULDERS) + ",\n"
    new_block += format_group("arms", ARMS) + "\n"
    new_block += "};"

    # Match from "const EXERCISES = {" to "};" followed by "// App state"
    pattern = r"const EXERCISES = \{.*?\};\n\n// App state"
    if not re.search(pattern, html, re.DOTALL):
        print("Could not find EXERCISES block")
        return 1

    new_html = re.sub(pattern, new_block + "\n\n// App state", html, count=1, flags=re.DOTALL)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Replaced EXERCISES with 120 exercises (30 per group).")
    return 0


if __name__ == "__main__":
    exit(main())
