class RecordSender {
  constructor(url) {
    this.url = url;
  }
  async send(records) {
    console.log(records);
    if (records.length == 0) {
        throw new Error('No records');
    }
    const data = new FormData();
    records.forEach((record, i) => {
      console.log(`index ${i}: ${record}`);
      data.append("records[]", record, `record_${i}`);
    });

    return await fetch(this.url, {
      method: "POST",
      body: data,
    });
  }
}

export default RecordSender;
