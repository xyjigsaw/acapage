---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I'm pursuing my doctoral degree in Computer Science in <a href="https://www.acemap.info/"><img src='./images/acemap_logo.png' style='width: 4em; border-radius: 5px;'></a>, IIOT Lab, at Shanghai Jiao Tong University, where I have the honor to be supervised by [Prof. Luoyi Fu](https://www.cs.sjtu.edu.cn/~fu-ly/index.html) and [Prof. Xinbing Wang](https://www.cs.sjtu.edu.cn/~wang-xb/).

My research interests include **natural language processing**, **knowledge graphs** and **data mining**. Specifically, I am devoted to research of large language models and temporal knowledge graph.

What's more, welcome to my technical blog [OmegaXYZ](https://en.omegaxyz.com/) and [中文博客](https://www.omegaxyz.com/).


<!--
My research interest includes neural machine translation and computer vision. I have published more than 100 papers at the top international AI conferences with total <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'>google scholar citations <strong><span id='total_cit'>260000+</span></strong></a> (You can also use google scholar badge <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>).
-->


# 🔥 News
- *2024.09.27* &nbsp; 🎉 One paper got accepted at EMNLP 2024, one paper got accepted at NeurIPS 2024!
- *2024.06.17* &nbsp; Invited 💬 talk at "AI-Based Future IoT Technologies and Services 2024 Workshop" in Jeju, Korea.
- *2024.03.13* &nbsp; 🎉 A long paper is accepted by NAACL 2024 main conference.
- *2023.12.31* &nbsp; GeoGalactica, a 30b LLM for GeoScience 🌏 has been released.
- *2023.07.01* &nbsp; The public beta version of 🤖[DeepReport](https://idea.acemap.cn/) has been released. 
- *2023.05.02* &nbsp; 🎉 Two long papers are accepted by ACL 2023 main conference. 
- *2023.04.27* &nbsp; I am invited to give a 💬 talk for a [temporal graph (TG) reading group](https://www.cs.mcgill.ca/~shuang43/rg.html) held by McGill University, Mila, NEC Laboratories Europe and University of Mannheim.


# 📝 Publications <a href='https://scholar.google.com/citations?user=E-VwoYEAAAAJ&hl=en'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>

- <span class='paper-badge'>EMNLP 2024</span> **RepEval: Effective Text Evaluation with LLM Representation**<br>
*Shuqian Sheng, <u><b>Yi Xu</b></u>, Tianhang Zhang, Zanwei Shen, Luoyi Fu, Jiaxin Ding, Lei Zhou, Xinbing Wang, Chenghu Zhou*<br>
In: *Conference on Empirical Methods in Natural Language Processing*, 2024 (CCF-B, main conference, long paper)<br>
<span class='paper-asset'><a href="https://arxiv.org/abs/2404.19563">Page</a></span> <span class='paper-asset'><a href="https://arxiv.org/pdf/2404.19563">PDF</a></span>

- <span class='paper-prebadge'>arXiv 2024</span> **Good Idea or Not, Representation of LLM Could Tell**<br>
*<u><b>Yi Xu</b></u>, Bo Xue, Shuqian Sheng, Cheng Deng, Jiaxin Ding, Zanwei Shen, Luoyi Fu, Xinbing Wang, Chenghu Zhou*<br>
In: *arXiv (preprint)*, 2024<br>
<span class='paper-asset'><a href="https://arxiv.org/abs/2409.13712">Page</a></span> <span class='paper-asset'><a href="https://arxiv.org/pdf/2409.13712">PDF</a></span>

- <span class='paper-badge'>NeurIPS 2024</span> **Human-Readable Fingerprint for Large Language Models**<br>
*Boyi Zeng, Lizheng Wang, Yuncong Hu, <u><b>Yi Xu</b></u>, Chenghu Zhou, Xinbing Wang, Yu Yu, Zhouhan Lin*<br>
In: *Conference on Neural Information Processing Systems*, 2024 (CCF-A)<br>
<span class='paper-asset'><a href="https://arxiv.org/abs/2312.04828">Page</a></span> <span class='paper-asset'><a href="https://arxiv.org/pdf/2312.04828">PDF</a></span>

- <span class='paper-prebadge'>arXiv 2024</span> **Unlock the Power of Frozen LLMs in Knowledge Graph Completion**<br>
*Bo Xue, <u><b>Yi Xu</b></u>, Yunchong Song, Yiming Pang, Yuyang Ren, Jiaxin Ding, Luoyi Fu, Xinbing Wang*<br>
In: *arXiv (preprint)*, 2024<br>
<span class='paper-asset'><a href="https://arxiv.org/abs/2408.06787">Page</a></span> <span class='paper-asset'><a href="https://arxiv.org/pdf/2408.06787">PDF</a></span>

- <span class='paper-badge'>NAACL 2024</span> **Is Reference Necessary in the Evaluation of NLG Systems? When and Where?**<br>
*Shuqian Sheng, <u><b>Yi Xu</b></u>, Luoyi Fu, Jiaxin Ding, Lei Zhou, Xinbing Wang, Chenghu Zhou*<br>
In: *The North American Chapter of the Association for Computational Linguistics*, 2024 (CCF-B, main conference, long paper)<br>
<span class='paper-asset'><a href="https://arxiv.org/abs/2403.14275">Page</a></span> <span class='paper-asset'><a href="https://arxiv.org/pdf/2403.14275">PDF</a></span>

- <span class='paper-prebadge'>arXiv 2024</span> **GeoGalactica: A Scientific Large Language Model in Geoscience**<br>
*Zhouhan Lin, Cheng Deng, Le Zhou, Tianhang Zhang, <u><b>Yi Xu</b></u>, Yutong Xu, Zhongmou He, Yuanyuan Shi, Beiya Dai, Yunchong Song, Boyi Zeng, Qiyuan Chen, Tao Shi, Tianyu Huang, Yiwei Xu, Shu Wang, Luoyi Fu, Weinan Zhang, Junxian He, Chao Ma, Yunqiang Zhu, Xinbing Wang, Chenghu Zhou*<br>
In: *arXiv (preprint)*, 2024<br>
<span class='paper-asset'><a href="https://arxiv.org/abs/2401.00434">Page</a></span> <span class='paper-asset'><a href="https://arxiv.org/pdf/2401.00434">PDF</a></span>

- <span class='paper-badge'>WSDM 2024</span> **Learning A Foundation Language Model for Geoscience Knowledge Understanding and Utilization**<br>
*Cheng Deng, Tianhang Zhang, Zhongmou He, <u><b>Yi Xu</b></u>, Qiyuan Chen, Yuanyuan Shi, Luoyi Fu, Weinan Zhang, Xinbing Wang, Chenghu Zhou, Zhouhan Lin and Junxian He*<br>
In: *ACM International Conference on Web Search and Data Mining*, 2024 (CCF-B)<br>
<span class='paper-asset'><a href="https://arxiv.org/abs/2306.05064">Page</a></span> <span class='paper-asset'><a href="https://arxiv.org/pdf/2306.05064.pdf">PDF</a></span>

- <span class='paper-badge'>ACL 2023</span> **Exploring and Verbalizing Academic Ideas by Concept Co-occurrence**<br>
*<u><b>Yi Xu</b></u>, Shuqian Sheng, Bo Xue, Luoyi Fu, Xinbing Wang and Chenghu Zhou*<br>
In: *Annual Meeting of the Association for Computational Linguistics*, 2023 (CCF-A, main conference, long paper)<br>
<span class='paper-asset'><a href="https://arxiv.org/abs/2306.02282">Page</a></span> <span class='paper-asset'><a href="https://arxiv.org/pdf/2306.02282">PDF</a></span> <span class='paper-asset'><a href="https://github.com/xyjigsaw/Kiscovery">Code</a></span>

- <span class='paper-badge'>ACL 2023</span> **Unsupervised Graph-Text Mutual Conversion with a Unified Pretrained Language Model**<br>
*<u><b>Yi Xu</b></u>, Shuqian Sheng, Jiexing Qi, Luoyi Fu, Zhouhan Lin, Xinbing Wang and Chenghu Zhou*<br>
In: *Annual Meeting of the Association for Computational Linguistics*, 2023 (CCF-A, main conference, long paper)<br>
<span class='paper-asset'><a href="https://aclanthology.org/2023.acl-long.281/">Page</a></span> <span class='paper-asset'><a href="https://aclanthology.org/2023.acl-long.281.pdf">PDF</a></span>

- <span class='paper-badge'>AAAI 2023</span> **Temporal Knowledge Graph Reasoning with Historical Contrastive Learning**<br>
*<u><b>Yi Xu</b></u>, Junjie Ou, Hui Xu, and Luoyi Fu*<br>
In: *AAAI Conference on Artificial Intelligence*, 2023 (CCF-A, <span style="color:red">Oral</span>)<br>
<span class='paper-asset'><a href="https://ojs.aaai.org/index.php/AAAI/article/view/25601">Page</a></span> <span class='paper-asset'><a href="https://arxiv.org/pdf/2211.10904">PDF</a></span> <span class='paper-asset'><a href="https://mp.weixin.qq.com/s/qDw3W282gDk-9nw7rkWphQ">Media</a></span> <span class='paper-asset'><a href="https://github.com/xyjigsaw/CENET">Code</a></span>

- <span class='paper-prebadge'>arXiv 2023</span> **Exploring the Limits of Historical Information for Temporal Knowledge Graph Extrapolation**<br>
*<u><b>Yi Xu</b></u>, Junjie Ou, Hui Xu, Luoyi Fu, Lei Zhou, Xinbing Wang and Chenghu Zhou*<br>
In: *arXiv (preprint)*, 2023<br>
<span class='paper-asset'><a href="https://arxiv.org/abs/2308.15002">Page</a></span> <span class='paper-asset'><a href="https://arxiv.org/pdf/2308.15002.pdf">PDF</a></span> <span class='paper-asset'><a href="https://mp.weixin.qq.com/s/qDw3W282gDk-9nw7rkWphQ">Media</a></span> <span class='paper-asset'><a href="https://github.com/xyjigsaw/CENET">Code</a></span>

- <span class='paper-prebadge'>arXiv 2022</span> **INFINITY: A Simple Yet Effective Unsupervised Framework for Graph-Text Mutual Conversion**<br>
*<u><b>Yi Xu</b></u>, Luoyi Fu, Zhouhan Lin, Jiexing Qi, and Xinbing Wang*<br>
In: *arXiv (preprint)*, 2022<br>
<span class='paper-asset'><a href="https://arxiv.org/abs/2209.10754">Page</a></span> <span class='paper-asset'><a href="https://arxiv.org/pdf/2209.10754">PDF</a></span>

- <span class='paper-badge'>TCYB 2021</span> **A Steering-matrix-based Multi-objective Evolutionary Algorithm for High-Dimensional Feature Selection**<br>
*Fan Cheng, Feixiang Chu, <u><b>Yi Xu</b></u>, and Lei Zhang*<br>
In: *IEEE Transactions on Cybernetics*, 2021 (SCI-Q1, IF:19.118, CCF-B)<br>
<span class='paper-asset'><a href="https://ieeexplore.ieee.org/abstract/document/9371430/), [PDF](https://drive.google.com/file/u/0/d/13xAz8dMIsU9TUfdeiP0JMCpvzxwzviwL/view">Page</a></span> <span class='paper-asset'><a href="https://drive.google.com/file/u/0/d/13xAz8dMIsU9TUfdeiP0JMCpvzxwzviwL/view">PDF</a></span> <span class='paper-asset'><a href="https://github.com/BIMK/SM-MOEA">Code</a></span>

- <span class='paper-badge'>ICIC 2019</span> **A Diversity based Competitive Multi-objective PSO for Feature Selection**<br>
*Jianfeng Qiu, Fan Cheng, Lei Zhang, and <u><b>Yi Xu</b> (Corresponding Author)</u>*<br>
In: *International Conference on Intelligent Computing*, 2019 (CCF-C, <span style="color:red">Oral</span>)<br>
<span class='paper-asset'><a href="https://link.springer.com/chapter/10.1007/978-3-030-26969-2_3">Page</a></span>

<span style="color:grey; padding-left:5px;">Two papers submitted to CCF-A conference/Journal are under review now.</span>



# 🚀 Projects

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">BETA</div><img src='images/deepreport.png' alt="sym"></div></div>
<div class='paper-box-text' markdown="1">

### [DeepReport Beta](https://idea.acemap.cn/)

Supported by the [Deep-time Digital Earth (DDE) International Big Science Program](https://www.ddeworld.org/), we develop DeepReport to inspire researchers for knowledge discovery. DeepReport provides functions such as paper retrieval, insights extraction, concept exploration, knowledge summarization and generation.
</div>
</div>


<!--

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2016</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Deep Residual Learning for Image Recognition](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)

**Kaiming He**, Xiangyu Zhang, Shaoqing Ren, Jian Sun

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
</div>
</div>
-->


<!--
# 🎖 Honors and Awards
- *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 


# 📖 Educations
- *2019.06 - 2022.04 (now)*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2015.09 - 2019.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
-->

# 📖 Services
### [Journal Reviewer](https://www.webofscience.com/wos/author/record/HJG-4521-2022)
- IEEE Transactions on Network Science and Engineering
- China Communications

### Conference Reviewer
- 2024: ACL-ARR (ACL, EMNLP)
- 2023: ACL, EMNLP, SIGMETRICS
- 2022: AAAI, SIGMETRICS


# 📚 Teaching
- Teaching Assistant,  Introduction to Engineering for Electronic Information, Shanghai Jiao Tong University (Fall 2023)
- Teaching Assistant, Data Structure and Algorithm (IEEE Class), Shanghai Jiao Tong University (Fall 2022)
- Teaching Assistant, Mobile Internet, Shanghai Jiao Tong University (Spring 2022)
- Teaching Assistant, Data Structure and Algorithm, Shanghai Jiao Tong University (Fall 2021)
- Teaching Assistant, Thinking and Approach of Programming, Shanghai Jiao Tong University (Fall 2020)


<!--
# 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/)


# 💻 Internships
- *2019.05 - 2020.02*, [Lorem](https://github.com/), China.
-->
