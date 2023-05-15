from alien_invasion import AlienInversion


"""
功能完善
功能1：增加开始游戏/重新开始的banner和按钮
功能2：增加游戏暂停和开始功能
功能3：飞船被外星人撞击之后，记分重新开始
"""
if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInversion()
    ai.run_game()
