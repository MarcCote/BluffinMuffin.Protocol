# Game : PlayerWonPot

BluffinMuffin.Protocol.Game.PlayerWonPotCommand

## PlayerWonPotCommand

### Command Schema

```json
{
  "title": "Schema for PlayerWonPotCommand",
  "type": "BluffinMuffin.Protocol.Game.PlayerWonPotCommand",
  "properties": {
    "CommandName": {
      "description": "Always contains 'PlayerWonPotCommand' to distinguish the command from others.",
      "type": "string"
    },
    "PlayerMoney": {
      "type": "int"
    },
    "PlayerPos": {
      "type": "int"
    },
    "PotId": {
      "type": "int"
    },
    "Shared": {
      "type": "int"
    },
    "TableId": {
      "type": "int"
    }
  }
}
```

### Example

```json
{
  "CommandName": "PlayerWonPotCommand",
  "PlayerPos": 0,
  "PotId": 0,
  "Shared": 0,
  "PlayerMoney": 0,
  "TableId": 0
}
```
