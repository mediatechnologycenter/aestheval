#from aestheval.sentiment_analysis.sentiment_score import *
from aestheval.baselines.run_baseline import run


if __name__ == "__main__":
#    sentiment_pccd()
#    sentiment_reddit()
#    sentiment_ava()
#    run('Reddit', 'nima')
#    run('PCCD', 'nima')
#    run('PCCD', 'mlsp')
    run('Reddit', 'mlsp')
    run('AVA', 'mlsp')
    run('AVA', 'nima')
    run('PCCD', 'vit')
    run('Reddit', 'vit')
    run('AVA', 'vit')
