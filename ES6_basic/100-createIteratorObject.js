export default function createIteratorObject(report) {
  const departments = Object.values(report.allEmployees);
  const employees = departments.flatMap((department) => department);

  let currentIndex = 0;

  return {
    next() {
      if (currentIndex < employees.length) {
        return {
          value: employees[currentIndex++],
          done: false,
        };
      } else {
        return {
          done: true,
        };
      }
    },
    [Symbol.iterator]() {
      return this;
    },
  };
}
