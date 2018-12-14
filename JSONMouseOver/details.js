window.onload = () => {
  const details = [
    {
      department: 'ISE',
      name: 'Hemant Joshi',
      usn: '1MS16IS137',
      year: '20/09/16',
    },
    {
      department: 'ISE',
      name: 'Elliot Alderson',
      usn: 'fscoitey0',
      year: '20/09/16',
    },
    {
      department: 'ISE',
      name: 'Thanos',
      usn: '0.50.50.50.5',
      year: '19/09/16',
    },
    {
      department: 'ISE',
      name: 'Vito Corleone',
      usn: '18181818',
      year: '20/09/72',
    },
  ];

  details.forEach((item, index) => {
    const listElement = document.createElement('th');
    listElement.onmouseover = () => {
      document.getElementById('name').innerHTML = details[index].name;
      document.getElementById('dept').innerHTML = details[index].department;
      document.getElementById('usn').innerHTML = details[index].usn;
      document.getElementById('year').innerHTML = details[index].year;
    };
    listElement.innerHTML = item.name;
    document.getElementById('menu').appendChild(listElement);
  });
}
