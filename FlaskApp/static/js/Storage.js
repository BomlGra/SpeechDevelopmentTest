class RecordStorage {
  records = [];
  add(record) {
    this.records.push(record);
  }
  getRecords() {
    return this.records;
  }
  clear() {
    this.records = [];
    console.log("A list of records cleared");
  }
}

export default RecordStorage;
