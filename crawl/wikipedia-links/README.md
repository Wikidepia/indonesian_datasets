# Wikipedia Links

[[Dataset Download](https://le4-0-66landstalker.pulsedmedia.com/public-sorechai/public_indonesian_datasets/wikipedia-links.tar.zst)]

Wikipedia have a lot of references & citations from internet. It should contain some high quality web content, this dataset contains 58k urls from Indonesian Wikipedia external links dump.

You will need to install [lm_dataformat](https://pypi.org/project/lm-dataformat/) to use it.

```python
from lm_dataformat import Reader

rdr = Reader('wikipedia-links')

for doc in rdr.stream_data():
    print(doc)
```
