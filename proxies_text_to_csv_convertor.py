from streamlit_tools import *
from proxies_text_to_csv_formatter import proxies_text_to_csv


def main():
    st.title('🎊Proxies Text to CSV Format App🎉')
    st.info('📤Please upload one file at least📤')
    uploaded_files = st.file_uploader('👇👇👇👇👇👇👇👇👇👇')

    df = pd.DataFrame()
    name = None
    if uploaded_files is not None:
        df = proxies_text_to_csv(uploaded_files)
        name = uploaded_files.name
        st.dataframe(df)

    st.download_button(
        label='📥Click on me to download the result📥',
        data=df.to_csv(index=False),
        file_name=f'{name}.csv',
        mime='txt/csv'
    )


if __name__ == '__main__':
    main()