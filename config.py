from dataclasses import dataclass
from environs import Env

@dataclass
class NewsettemerConfig:
    default_value_h: int
    default_value_min: int
    default_value_s: int
    default_value_music: str



@dataclass
class Config:
    N_C: NewsettemerConfig
    def __str__(self)->str:
        return f'В классе собраны данные о первоначальных настройках'
    
def load_config(path: str | None = None)->Config:
    # Создаем экземпляр класса Env
    env: Env = Env()
    # Добавляем переменные окружения в среду окружения (path - путь к файлу .env)
    env.read_env(path)

    # Создаем экземпляр класса Config
    return Config(N_C=NewsettemerConfig(default_value_h=env.int('DEF_VALUE_H'),
            default_value_min=env.int('DEF_VALUE_MIN'),
            default_value_s=env.int('DEF_VALUE_S'),
            default_value_music=env('MUSIC')))
if __name__ == '__main__':
    config = load_config(".env_newsettimer")
    # Выводим значения полей экземпляра класса Config на печать,
    # чтобы убедиться, что все данные, получаемые из переменных окружения доступны
    print(config.N_C.default_value_h)
    print(config.N_C.default_value_min)
    print(config.N_C.default_value_s)
    print(config.N_C.default_value_music)
   