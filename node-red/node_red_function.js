const minMaxF1 = [ 8, 17 ];
const minMaxF2 = [ 6, 17 ];
const minMaxF3 = [ 9, 20 ];
const minMaxF4 = [ 9, 20 ];
const minMaxF5 = [ 8.5, 20 ];

return [
    msg,
    { payload : minMaxF1[1] - (minMaxF1[1]-minMaxF1[0]) * msg.req.query.f1 / 100  },
    { payload : minMaxF2[1] - (minMaxF2[1]-minMaxF2[0]) * msg.req.query.f2 / 100  },
    { payload : minMaxF3[1] - (minMaxF3[1]-minMaxF3[0]) * msg.req.query.f3 / 100  },
    { payload : minMaxF4[1] - (minMaxF4[1]-minMaxF4[0]) * msg.req.query.f4 / 100  },
    { payload : minMaxF5[1] - (minMaxF5[1]-minMaxF5[0]) * msg.req.query.f5 / 100  },
];
