def test():
    print(
    f"{'Trades:':<15}{cnt:>10}",
    f"\n{'Wins:':<15}{wins:>10}",
    f"\n{'Losses:':<15}{losses:>10}",
    f"\n{'Breakeven:':<15}{evens:>10}",
    f"\n{'Win/Loss Ratio:':<15}{win_r:>10}",
    f"\n{'Mean Win:':<15}{mean_w:>10}",
    f"\n{'Mean Loss:':<15}{mean_l:>10}",
    f"\n{'Mean:':<15}{mean_trd:>10}",
    f"\n{'Std Dev:':<15}{sd:>10}",
    f"\n{'Max Loss:':<15}{max_l:>10}",
    f"\n{'Max Win:':<15}{max_w:>10}",
    f"\n{'Sharpe Ratio:':<15}{sharpe_r:>10}",
)
test()