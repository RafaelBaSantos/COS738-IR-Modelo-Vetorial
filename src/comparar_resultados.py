import matplotlib.pyplot
import pandas as pd
from configparser import ConfigParser

from nltk.metrics.scores import precision, recall, f_measure
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt

config = ConfigParser()
config.read(r'.\config\AVALIA.CFG')

LEIA_DIR = config.get("avalia", 'LEIA_DIR')
LEIA_ESPERADOS = config.get("avalia", 'LEIA_ESPERADOS')

df_stem = pd.read_csv(LEIA_DIR + r"\RESULTADOS-STEMMER.csv", sep=";")
df_no_stem = pd.read_csv(LEIA_DIR + r"\RESULTADOS-NOSTEMMER.csv", sep=";")
df_esperados = pd.read_csv(LEIA_ESPERADOS, sep=";")
df_esperados = df_esperados.sort_values(["QueryNumber", "DocVote"], ascending=False)


def precision_recall_11_point(df_resultados, df_esperados):
    ls_df_scores = []
    for query_number in df_esperados["QueryNumber"].unique():
        df_resultados_local = df_resultados[df_resultados["QueryNumber"] == query_number]
        df_esperados_local = df_esperados[df_esperados["QueryNumber"] == query_number]
    
        set_esperados = set(df_esperados_local["DocNumber"].values)
    
        ls_precisao = []
        ls_revocacao = []
        set_records = set()
        last_recall = 0
        for idx, row in df_resultados_local.iterrows():
            set_records.add(row["RecordNum"])
    
            recall_local = recall(set_esperados, set_records)
            if recall_local == last_recall:
                continue
    
            precision_local = precision(set_esperados, set_records)
    
            ls_precisao.append(precision_local)
            ls_revocacao.append(recall_local)
    
            if recall_local == 1:
                break
    
            last_recall = recall_local
    
        df_scores_local = pd.DataFrame({"Precisão": ls_precisao, "Revocação": ls_revocacao})
    
        ls_precisao = []
        ls_revocacao = []
        for revocacao in (np.array(range(11)) / 10):
            ls_revocacao.append(revocacao)
            ls_precisao.append(df_scores_local.loc[(df_scores_local["Revocação"] >= revocacao), "Precisão"].max())
    
        df_scores_local = pd.DataFrame({"Precisão": ls_precisao, "Revocação": ls_revocacao})
        df_scores_local["QueryNumber"] = query_number
        ls_df_scores.append(df_scores_local)

    df_scores = pd.concat(ls_df_scores)

    df_scores = df_scores.fillna(0)

    return df_scores


df_onze_pontos_nostem = precision_recall_11_point(df_no_stem, df_esperados)
df_onze_pontos_stem = precision_recall_11_point(df_stem, df_esperados)

plt.subplot(1, 2, 1)
sb.lineplot(df_onze_pontos_nostem, x="Revocação", y="Precisão", hue="QueryNumber")
plt.subplot(1, 2, 2)
sb.lineplot(df_onze_pontos_stem, x="Revocação", y="Precisão", hue="QueryNumber")


def f_1(df_resultados, df_esperados):
    ls_query_number = []
    ls_f_1 = []
    for query_number in df_esperados["QueryNumber"].unique():
        df_resultados_local = df_resultados[df_resultados["QueryNumber"] == query_number]
        df_esperados_local = df_esperados[df_esperados["QueryNumber"] == query_number]

        if df_esperados_local.shape[0] >= 10:
            set_esperados = set(df_esperados_local.iloc[0:10]["DocNumber"].values)
            set_resultados = set(df_resultados_local.iloc[0:10]["RecordNum"].values)

        else:
            set_esperados = set(df_esperados_local["DocNumber"].values)
            set_resultados = set(df_resultados_local.iloc[0:len(set_esperados)]["RecordNum"].values)

        f_1 = f_measure(set_esperados, set_resultados, alpha=0.5)

        ls_query_number.append(query_number)
        ls_f_1.append(f_1)

    df_score = pd.DataFrame({"QueryNumber": ls_query_number, "f_1": ls_f_1})
    return df_score


df_f_1_nostem = f_1(df_no_stem, df_esperados)
avg_f_1_nostem = df_f_1_nostem.f_1.mean()

df_f_1_stem = f_1(df_stem, df_esperados)
avg_f_1_stem = df_f_1_stem.f_1.mean()


def precision_at_n(df_resultados, df_esperados, n):
    ls_query_number = []
    ls_p_5 = []
    for query_number in df_esperados["QueryNumber"].unique():
        df_resultados_local = df_resultados[df_resultados["QueryNumber"] == query_number]
        df_esperados_local = df_esperados[df_esperados["QueryNumber"] == query_number]

        if df_esperados_local.shape[0] >= n:
            set_esperados = set(df_esperados_local.iloc[0:n]["DocNumber"].values)
            set_resultados = set(df_resultados_local.iloc[0:n]["RecordNum"].values)
        else:
            set_esperados = set(df_esperados_local["DocNumber"].values)
            set_resultados = set(df_resultados_local.iloc[0:len(set_esperados)]["RecordNum"].values)

        p_5 = precision(set_esperados, set_resultados)

        ls_query_number.append(query_number)
        ls_p_5.append(p_5)

    df_score = pd.DataFrame({"QueryNumber": ls_query_number, "Precision@n": ls_p_5})
    return df_score


df_p_5_nostem = precision_at_n(df_no_stem, df_esperados, 5)
avg_p_5_nostem = df_p_5_nostem["Precision@n"].mean()

df_p_5_stem = precision_at_n(df_stem, df_esperados, 5)
avg_p_5_stem = df_p_5_stem["Precision@n"].mean()

df_p_10_nostem = precision_at_n(df_no_stem, df_esperados, 10)
avg_p_10_nostem = df_p_10_nostem["Precision@n"].mean()

df_p_10_stem = precision_at_n(df_stem, df_esperados, 10)
avg_p_10_stem = df_p_10_stem["Precision@n"].mean()

ls_r_precision = []
for n in range(1225):
    df_p_5_nostem = precision_at_n(df_no_stem, df_esperados, 5)
    avg_p_5_nostem = df_p_5_nostem["Precision@n"].mean()

    df_p_5_stem = precision_at_n(df_stem, df_esperados, 5)
    avg_p_5_stem = df_p_5_stem["Precision@n"].mean()
