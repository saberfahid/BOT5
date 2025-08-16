
from sigma_bot.handler import generate_sigma_message
from math_bot.handler import generate_math_message
from fitness_bot.handler import generate_fitness_message
from travel_bot.handler import generate_travel_message
from kokobot.handler import generate_koko_message
from core.bot_manager import BotManager

def sigma_bot_handler(user_message):
    return generate_sigma_message(user_message)

def math_bot_handler(user_message):
    return generate_math_message(user_message)

def fitness_bot_handler(user_message):
    return generate_fitness_message(user_message)

def travel_bot_handler(user_message):
    return generate_travel_message(user_message)

def kokobot_handler(user_message):
    return generate_koko_message(user_message)

def main():
    print("""
Welcome to Multi-Bot System!
All bots will reply to your message at the same time.
Type 'exit' to quit.
""")
    manager = BotManager()
    manager.register_bot("💝 Sigma", sigma_bot_handler)
    manager.register_bot("🔢 Math", math_bot_handler)
    manager.register_bot("💪 Fitness", fitness_bot_handler)
    manager.register_bot("✈️ Travel", travel_bot_handler)
    manager.register_bot("🌐 Koko", kokobot_handler)
    while True:
        user_message = input("Enter your message: ").strip()
        if user_message.lower() == 'exit':
            print("Goodbye!")
            break
        manager.run_all(user_message)

if __name__ == "__main__":
    main()
