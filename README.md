# Shift-Reduce Task-Oriented Semantic Parsing with Stack-Transformers
This repository includes the code of the in-order shift-reduce approach for task-oriented semantic parsing described in paper [Shift-Reduce Task-Oriented Semantic Parsing with Stack-Transformers](https://arxiv.org/pdf/2210.11984.pdf). This implementation is based on the system by [Fernandez Astudillo et al. (2020)](https://www.aclweb.org/anthology/2020.findings-emnlp.89) and reuses part of its [code](https://github.com/IBM/transition-amr-parser/tree/stack-transformer).


## Requirements
This implementation was tested on Python 3.6.9, PyTorch 1.1.0 and CUDA 9.0.176. Please run the following command to proceed with the installation:
``` 
    cd ShiftReduce-TOP
    pip install -r requirements.txt
```


## Data
Standard train, test and development splits from the [TOP dataset](http://fb.me/semanticparsingdialog) were already included in the ``DATA`` folder.

## Experiments
To train a model for the TOP dataset, just execute the following script:
``` 
   ./scripts/stack-transformer/con_experiment.sh configs/top_roberta.large.sh
```

To test the trained model on the test split, please run the following command:
``` 
    ./scripts/stack-transformer/con_test-test.sh config/test_roberta_large.sh DATA/dep-parsing/models/TOP_RoBERTa-large_stnp6x6-seed44/checkpoint_top3-average.pt DATA/dep-parsing/models/TOP_RoBERTa-large_stnp6x6-seed44/epoch-tests-test/dec-checkpoint-top3-average
``` 


## Citation
```
@misc{fernándezgonzález2022shiftreduce,
      title={Shift-Reduce Task-Oriented Semantic Parsing with Stack-Transformers}, 
      author={Daniel Fernández-González},
      year={2022},
      eprint={2210.11984},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## Acknowledgments

We have received funding from grant SCANNER-UDC (PID2020-113230RB-C21) funded by MCIN/AEI/10.13039/501100011033, Xunta de Galicia (ED431C 2020/11), and Centro de Investigación de Galicia "CITIC", funded by Xunta de Galicia and the European Union (ERDF - Galicia 2014-2020 Program), by grant ED431G 2019/01.                                                                                                                                   
