# Missile
epic gamer cool missile sim thing

![example image](img/game.png)

## thingamajigs
- missile ![missile](img/missile.png)
- enemy ![enemy](img/enemy.png)
- target ![target](img/target.png)

## guidance types
| object   | type       | description                                 | progress | effectiveness |
|----------|------------|---------------------------------------------|----------|---------------|
| missile  | direct     | go to nearest target                        | 100% 👍 | 75% ✅        |
| enemy    | direct     | go to nearest missile                       | 100% 👍 | 50% ➖        |
| enemy    | predictive | go to where the nearest missile will be     | 60% 👌  | ??%❓         |
| enemy    | defensive  | go to the missile closest to nearest target | 0% 👎   | ??%❓         |
| target   | static     | dont move                                   | 100% 👍 | 0% ❌         |
