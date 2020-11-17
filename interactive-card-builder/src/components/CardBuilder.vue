<template>
  <div class="container">
    <div class="card mx-auto shadow-lg border-0 p-2">
      <div class="row">
        <div class="col-sm-6 col-md-5">
          <div class="card-body">
            <form>
              <div class="form-row">
                <div class="form-group col-md-6">
                  <label for="inputEmail4">First Name</label>
                  <input type="text" class="form-control" v-model="firstName" />
                </div>
                <div class="form-group col-md-6">
                  <label for="inputPassword4">Last Name</label>
                  <input type="text" class="form-control" v-model="lastName" />
                </div>
              </div>

              <div class="form-row">
                <div class="form-group col-md-12">
                  <label for="inputPassword4">Company</label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="job.company"
                  />
                </div>

                <div class="form-group col-md-12">
                  <label for="inputPassword4">Position</label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="job.position"
                  />
                </div>
              </div>

              <div class="form-row">
                <div class="form-group col-md-6">
                  <label for="inputPassword4">Salary</label>
                  <input
                    type="email"
                    class="form-control"
                    v-model="job.salary"
                  />
                </div>
                <div class="form-group col-md-6">
                  <label for="inputZip">Age</label>
                  <input
                    type="tel"
                    class="form-control"
                    v-model="job.age"
                  />
                </div>
              </div>

              <button
                type="button"
                class="btn btn-primary btn-block"
                @click="getData()"
              >
                Get Data
              </button>
            </form>
          </div>
        </div>
        <div class="col-sm-6 col-md-6 mx-auto">
          <div class="card-design">
            <div class="front-side">
              <h4>{{ firstName }} {{ lastName }}</h4>
              <p class="h6">{{ job.position }}</p>
              <p class="h6">{{ job.company }}</p>
              <p class="h6">{{ job.email }}</p>
              <p class="h6">{{ job.salary }}</p>
              <p class="h6">{{ job.age }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <table class="table">
      <thead class="thead-dark">
        <tr>
          <th scope="col">#</th>
          <th scope="col">Name</th>
          <th scope="col">Company</th>
          <th scope="col">Position</th>
          <th scope="col">Salary</th>
          <th scope="col">Age</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="info in infos" :key="info.id">
          <th scope="row">{{info.id}}</th>
          <td>{{info.name}}</td>
          <td>{{info.office}}</td>
          <td>{{info.position}}</td>
          <td>{{info.salary}}</td>
          <td>{{info.age}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Card Builder",
  data() {
    return {
      firstName: "Brack",
      lastName: "Obama",
      job: {
        company: "Early Advantage",
        position: "Lead Software Engineer",
        salary: 230000,
        age: 67,
      },
      data: {
        id: null,
        name: "",
        position: "",
        office: "",
        age: null,
        salary: "",
      },
      infos: [
        {
          id: 1,
          name: "John Doe",
          position: "CTO",
          office: "Tejgaon",
          age: 80,
          salary: "80000",
        },
        {
          id: 2,
          name: "Ratul bhaia",
          position: "Engineer",
          office: "Tejgaon",
          age: 90,
          salary: "900000",
        },
        {
          id: 3,
          name: "Tiger Nixon",
          position: "System Architect",
          office: "Edinburgh",
          age: 20,
          salary: "$320,800",
        },
        {
          id: 4,
          name: "Garrett Winters",
          position: "Accountant",
          office: "Tokyo",
          age: 21,
          salary: "$170,750",
        },
        {
          id: 5,
          name: "Ashton Cox",
          position: "Junior Technical Author",
          office: "San Francisco",
          age: 22,
          salary: "$86,000",
        },
        {
          id: 6,
          name: "Cedric Kelly",
          position: "Senior Javascript Developer",
          office: "Edinburgh",
          age: 23,
          salary: "$433,060",
        },
        {
          id: 7,
          name: "Airi Satou",
          position: "Accountant",
          office: "Tokyo",
          age: 24,
          salary: "$162,700",
        },
        {
          id: 8,
          name: "Brielle Williamson",
          position: "Integration Specialist",
          office: "New York",
          age: 25,
          salary: "$372,000",
        },
        {
          id: 9,
          name: "Herrod Chandler",
          position: "Sales Assistant",
          office: "San Francisco",
          age: 26,
          salary: "$137,500",
        },
        {
          id: 10,
          name: "Rhona Davidson",
          position: "Integration Specialist",
          office: "Tokyo",
          age: 27,
          salary: "$327,900",
        },
        {
          id: 11,
          name: "Colleen Hurst",
          position: "Javascript Developer",
          office: "San Francisco",
          age: 28,
          salary: "$205,500",
        },
        {
          id: 12,
          name: "Sonya Frost",
          position: "Software Engineer",
          office: "Edinburgh",
          age: 29,
          salary: "$103,600",
        },
        {
          id: 13,
          name: "Jena Gaines",
          position: "Office Manager",
          office: "London",
          age: 30,
          salary: "$90,560",
        },
        {
          id: 14,
          name: "Quinn Flynn",
          position: "Support Lead",
          office: "Edinburgh",
          age: 31,
          salary: "$342,000",
        },
        {
          id: 15,
          name: "Charde Marshall",
          position: "Regional Director",
          office: "San Francisco",
          age: 32,
          salary: "$470,600",
        },
        {
          id: 16,
          name: "Haley Kennedy",
          position: "Senior Marketing Designer",
          office: "London",
          age: 33,
          salary: "$313,500",
        },
        {
          id: 17,
          name: "Tatyana Fitzpatrick",
          position: "Regional Director",
          office: "London",
          age: 34,
          salary: "$385,750",
        },
        {
          id: 18,
          name: "Michael Silva",
          position: "Marketing Designer",
          office: "London",
          age: 35,
          salary: "$198,500",
        },
        {
          id: 19,
          name: "Paul Byrd",
          position: "Chief Financial Officer (CFO)",
          office: "New York",
          age: 36,
          salary: "$725,000",
        },
        {
          id: 20,
          name: "Gloria Little",
          position: "Systems Administrator",
          office: "New York",
          age: 37,
          salary: "$237,500",
        },
        {
          id: 21,
          name: "Bradley Greer",
          position: "Software Engineer",
          office: "London",
          age: 38,
          salary: "$132,000",
        },
        {
          id: 22,
          name: "Dai Rios",
          position: "Personnel Lead",
          office: "Edinburgh",
          age: 39,
          salary: "$217,500",
        },
        {
          id: 23,
          name: "Jenette Caldwell",
          position: "Development Lead",
          office: "New York",
          age: 40,
          salary: "$345,000",
        },
        {
          id: 24,
          name: "Yuri Berry",
          position: "Chief Marketing Officer (CMO)",
          office: "New York",
          age: 41,
          salary: "$675,000",
        },
        {
          id: 25,
          name: "Caesar Vance",
          position: "Pre-Sales Support",
          office: "New York",
          age: 42,
          salary: "$106,450",
        },
        {
          id: 26,
          name: "Doris Wilder",
          position: "Sales Assistant",
          office: "Sydney",
          age: 43,
          salary: "$85,600",
        },
        {
          id: 27,
          name: "Angelica Ramos",
          position: "Chief Executive Officer (CEO)",
          office: "London",
          age: 44,
          salary: "$1,200,000",
        },
        {
          id: 28,
          name: "Gavin Joyce",
          position: "Developer",
          office: "Edinburgh",
          age: 45,
          salary: "$92,575",
        },
        {
          id: 29,
          name: "Jennifer Chang",
          position: "Regional Director",
          office: "Singapore",
          age: 46,
          salary: "$357,650",
        },
        {
          id: 30,
          name: "Brenden Wagner",
          position: "Software Engineer",
          office: "San Francisco",
          age: 47,
          salary: "$206,850",
        },
        {
          id: 31,
          name: "Fiona Green",
          position: "Chief Operating Officer (COO)",
          office: "San Francisco",
          age: 48,
          salary: "$850,000",
        },
        {
          id: 32,
          name: "Shou Itou",
          position: "Regional Marketing",
          office: "Tokyo",
          age: 49,
          salary: "$163,000",
        },
        {
          id: 33,
          name: "Michelle House",
          position: "Integration Specialist",
          office: "Sydney",
          age: 50,
          salary: "$95,400",
        },
        {
          id: 34,
          name: "Suki Burks",
          position: "Developer",
          office: "London",
          age: 51,
          salary: "$114,500",
        },
        {
          id: 35,
          name: "Prescott Bartlett",
          position: "Technical Author",
          office: "London",
          age: 52,
          salary: "$145,000",
        },
        {
          id: 36,
          name: "Gavin Cortez",
          position: "Team Leader",
          office: "San Francisco",
          age: 53,
          salary: "$235,500",
        },
        {
          id: 37,
          name: "Martena Mccray",
          position: "Post-Sales support",
          office: "Edinburgh",
          age: 54,
          salary: "$324,050",
        },
        {
          id: 38,
          name: "Unity Butler",
          position: "Marketing Designer",
          office: "San Francisco",
          age: 55,
          salary: "$85,675",
        },
      ],
    };
  },
  methods: {
    getData() {
      //const API = `http://localhost:8000/api/employee_information/`
      axios
        .get("http://localhost:8000/api/employee_information/")
        .then((res) => {
          let val = res.data;
          // let info = {
          //     id: val.id,
          //     name: val.name,
          //     position: val.position,
          //     office: val.office,
          //     age: val.age,
          //     salary: val.salary
          // }
          // this.data = info
          console.log(val);
        })
        .catch(function (error) {
          // handle error
          console.log(error);
        });
    },
  },
};
</script>

<style>
</style>