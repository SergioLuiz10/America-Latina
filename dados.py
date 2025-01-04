import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df=pd.read_csv("C:\\Users\\sergi\\Downloads\\imigrantes_canada.csv")


def americaSul_4(pallet="tab10", style="whitegrid"):
    america_latina = df.query('País in ["Brasil", "Argentina", "Peru", "Colômbia"]')
    america_latina_sort = america_latina.sort_values(by="Total", ascending=True)
    
    sns.set_style(style=style)
    fig, ax = plt.subplots(figsize=(12, 4))
    ax = sns.barplot(data=america_latina_sort, y="País", x="Total", orient="h", palette=pallet, ax=ax)

    for i, v in enumerate(america_latina_sort["Total"]):
        ax.text(v + 20, i, str(v), va='center', fontsize=10, color='black')

    ax.set_title("Tendências de imigração dos 4 maiores países da América Latina para o Canadá", loc="left", fontsize=12)
    ax.set_xlabel("Total", fontsize=12)
    ax.set_ylabel("") 
    ax.tick_params(axis="y", labelsize=8)
    plt.savefig("tendencias_imigracao.png", dpi=300, bbox_inches="tight")
    plt.show()
   
americaSul_4()
