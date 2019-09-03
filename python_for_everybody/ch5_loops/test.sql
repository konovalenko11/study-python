-- -----------------------------------------------------
-- Online compilers
-- -----------------------------------------------------
-- https://rextester.com/l/sql_server_online_compiler
-- https://rextester.com/CSQU8047 -- ready schema

-- https://dbfiddle.uk/?rdbms=sqlserver_2017
-- https://dbfiddle.uk/?rdbms=sqlserver_2017&fiddle=5afedd23e65e2087e39f5feeabc96a67 -- ready schema

-- http://sqlfiddle.com (not always working)

-- -----------------------------------------------------
-- Schema (DDL)
-- -----------------------------------------------------
-- Departments information.
CREATE TABLE departments (
    [dep_id]            INTEGER         PRIMARY KEY,
    [name]              VARCHAR(100)    NOT NULL
);

-- Current Employee information.
CREATE TABLE employees (
    [emp_id]            INTEGER         PRIMARY KEY,
    [name]              VARCHAR(100)    NOT NULL,
    [dep_id]            INTEGER         NOT NULL,
    [manager_emp_id]    INTEGER         NOT NULL,
    FOREIGN KEY (dep_id) REFERENCES departments (dep_id),
    FOREIGN KEY (manager_emp_id) REFERENCES employees (emp_id)
);

-- Closed/Created tickets information.
CREATE TABLE tickets (
    [ticket_id]             INTEGER         PRIMARY KEY,
    [created_timestamp]     DATETIME2       NOT NULL,
    [closed_timestamp]      DATETIME2,
    [resolved_by_emp_id]    INTEGER,   -- ID of an employee who closed the ticket
    FOREIGN KEY (resolved_by_emp_id) REFERENCES employees (emp_id)
);

-- Employee historical attributes.
CREATE TABLE employee_history (
    [emp_id]                INTEGER     NOT NULL,
    [dep_id]                INTEGER     NOT NULL,
    [manager_emp_id]        INTEGER     NOT NULL,
    [row_eff_date_start]    DATE        NOT NULL, -- Date when the record began to be effective
    [row_eff_date_end]      DATE        NOT NULL, -- Date when the record stopped to be effective
    [curr_flag]             CHAR(1)     NOT NULL, -- Flag that indicates if the record is "current"/latest
    PRIMARY KEY (emp_id, row_eff_date_start),
    FOREIGN KEY (emp_id) REFERENCES employees (emp_id),
    FOREIGN KEY (manager_emp_id) REFERENCES employees (emp_id),
    FOREIGN KEY (dep_id) REFERENCES departments (dep_id)
);
-- GO

-- -----------------------------------------------------
-- Schema (DML)
-- -----------------------------------------------------
INSERT INTO departments (
    [dep_id], 
    [name]
)
VALUES
    (1, 'D1'),
    (2, 'D2'),
    (3, 'D3'),
    (4, 'D4'),
    (5, 'D5')
;

INSERT INTO employees (
    [emp_id], 
    [name],
    [dep_id],
    [manager_emp_id]
)
VALUES
    (10, 'Employee 10', 1, 10),
    (20, 'Employee 20', 2, 20),
    (30, 'Employee 30', 3, 30),
    (40, 'Employee 40', 4, 40),
    (50, 'Employee 50', 5, 50),
    (101, 'Employee 101', 1, 10),
    (102, 'Employee 102', 1, 10),
    (103, 'Employee 103', 1, 10),
    (104, 'Employee 104', 1, 10),
    (105, 'Employee 105', 1, 10),
    (106, 'Employee 106', 1, 10),
    (107, 'Employee 107', 1, 10),
    (108, 'Employee 108', 1, 10),
    (109, 'Employee 109', 1, 10),
    (110, 'Employee 110', 1, 10),
    (111, 'Employee 111', 2, 20),
    (112, 'Employee 112', 2, 20),
    (113, 'Employee 113', 2, 20),
    (114, 'Employee 114', 2, 20),
    (115, 'Employee 115', 2, 20),
    (116, 'Employee 116', 2, 20),
    (117, 'Employee 117', 2, 20),
    (118, 'Employee 118', 2, 20),
    (119, 'Employee 119', 2, 20),
    (120, 'Employee 120', 2, 20),
    (121, 'Employee 121', 3, 30),
    (122, 'Employee 122', 3, 30),
    (123, 'Employee 123', 3, 30),
    (124, 'Employee 124', 3, 30),
    (125, 'Employee 125', 3, 30),
    (126, 'Employee 126', 3, 30),
    (127, 'Employee 127', 3, 30),
    (128, 'Employee 128', 3, 30),
    (129, 'Employee 129', 3, 30),
    (130, 'Employee 130', 3, 30),
    (131, 'Employee 131', 4, 40),
    (132, 'Employee 132', 4, 40),
    (133, 'Employee 133', 4, 40),
    (134, 'Employee 134', 4, 40),
    (135, 'Employee 135', 4, 40),
    (136, 'Employee 136', 4, 40),
    (137, 'Employee 137', 4, 40),
    (138, 'Employee 138', 4, 40),
    (139, 'Employee 139', 4, 40),
    (140, 'Employee 140', 4, 40),
    (141, 'Employee 141', 5, 50),
    (142, 'Employee 142', 5, 50),
    (143, 'Employee 143', 5, 50),
    (144, 'Employee 144', 5, 50),
    (145, 'Employee 145', 5, 50),
    (146, 'Employee 146', 5, 50),
    (147, 'Employee 147', 5, 50),
    (148, 'Employee 148', 5, 50),
    (149, 'Employee 149', 5, 50),
    (150, 'Employee 150', 5, 50)
;


WITH cte AS (
    SELECT 
        1 AS ticket_id
    UNION ALL
    SELECT
        ticket_id + 1 AS ticket_id
    FROM
        cte
    WHERE
        ticket_id < 100
)
INSERT INTO tickets (
    [ticket_id], 
    [created_timestamp],
    [closed_timestamp],
    [resolved_by_emp_id]
)
SELECT 
    ROW_NUMBER() OVER (ORDER BY cte1.ticket_id) AS ticket_id,
    dateadd(day, -1 * (ABS(CHECKSUM(NewId())) % 240) - 240, CURRENT_TIMESTAMP) AS created_timestamp,
    -- generating closed dates as current date - random # of days (0 - 240)
    dateadd(day, -1 * (ABS(CHECKSUM(NewId())) % 240), CURRENT_TIMESTAMP) AS closed_timestamp,
    -- this will regulate the emp_id range. Currently designed to generate emp_id from 101 to 120 (D1 and D2)
    (ABS(CHECKSUM(NewId())) % 20) + 101 AS resolved_by_emp_id
FROM 
    cte AS cte1
CROSS JOIN
    cte AS cte2;


INSERT INTO employee_history (
    [emp_id], 
    [dep_id],
    [manager_emp_id],
    [row_eff_date_start],
    [row_eff_date_end],
    [curr_flag]
)
VALUES
    (10, 1, 10, '2016-01-01', '9999-12-31', 'Y'),
    (20, 2, 20, '2016-01-01', '9999-12-31', 'Y'),
    (30, 3, 30, '2016-01-01', '9999-12-31', 'Y'),
    (40, 4, 40, '2016-01-01', '9999-12-31', 'Y'),
    (50, 5, 50, '2016-01-01', '9999-12-31', 'Y'),
    (101, 1, 10, '2016-01-01', '9999-12-31', 'Y'),
    (102, 1, 10, '2016-01-01', '9999-12-31', 'Y'),
    (103, 1, 10, '2016-01-01', '9999-12-31', 'Y'),
    (104, 1, 10, '2016-01-01', '9999-12-31', 'Y'),

    (105, 2, 20, '2016-01-01', '2019-03-10', 'N'),
    (105, 1, 10, '2019-03-11', '9999-12-31', 'Y'),

    (106, 1, 10, '2016-01-01', '9999-12-31', 'Y'),
    (107, 1, 10, '2016-01-01', '9999-12-31', 'Y'),
    (108, 1, 10, '2016-01-01', '9999-12-31', 'Y'),
    (109, 1, 10, '2016-01-01', '9999-12-31', 'Y'),
    (110, 1, 10, '2016-01-01', '9999-12-31', 'Y'),

    (111, 1, 20, '2016-01-01', '2019-04-05', 'N'),
    (111, 2, 20, '2019-04-06', '9999-12-31', 'Y'),

    (112, 2, 20, '2016-01-01', '9999-12-31', 'Y'),
    (113, 2, 20, '2016-01-01', '9999-12-31', 'Y'),
    (114, 2, 20, '2016-01-01', '9999-12-31', 'Y'),
    (115, 2, 20, '2016-01-01', '9999-12-31', 'Y'),
    (116, 2, 20, '2016-01-01', '9999-12-31', 'Y'),
    (117, 2, 20, '2016-01-01', '9999-12-31', 'Y'),
    (118, 2, 20, '2016-01-01', '9999-12-31', 'Y'),
    (119, 2, 20, '2016-01-01', '9999-12-31', 'Y'),
    (120, 2, 20, '2016-01-01', '9999-12-31', 'Y'),
    (121, 3, 30, '2016-01-01', '9999-12-31', 'Y'),
    (122, 3, 30, '2016-01-01', '9999-12-31', 'Y'),
    (123, 3, 30, '2016-01-01', '9999-12-31', 'Y'),
    (124, 3, 30, '2016-01-01', '9999-12-31', 'Y'),
    (125, 3, 30, '2016-01-01', '9999-12-31', 'Y'),
    (126, 3, 30, '2016-01-01', '9999-12-31', 'Y'),
    (127, 3, 30, '2016-01-01', '9999-12-31', 'Y'),
    (128, 3, 30, '2016-01-01', '9999-12-31', 'Y'),
    (129, 3, 30, '2016-01-01', '9999-12-31', 'Y'),
    (130, 3, 30, '2016-01-01', '9999-12-31', 'Y'),
    (131, 4, 40, '2016-01-01', '9999-12-31', 'Y'),
    (132, 4, 40, '2016-01-01', '9999-12-31', 'Y'),
    (133, 4, 40, '2016-01-01', '9999-12-31', 'Y'),
    (134, 4, 40, '2016-01-01', '9999-12-31', 'Y'),
    (135, 4, 40, '2016-01-01', '9999-12-31', 'Y'),
    (136, 4, 40, '2016-01-01', '9999-12-31', 'Y'),
    (137, 4, 40, '2016-01-01', '9999-12-31', 'Y'),
    (138, 4, 40, '2016-01-01', '9999-12-31', 'Y'),
    (139, 4, 40, '2016-01-01', '9999-12-31', 'Y'),
    (140, 4, 40, '2016-01-01', '9999-12-31', 'Y'),
    (141, 5, 50, '2016-01-01', '9999-12-31', 'Y'),
    (142, 5, 50, '2016-01-01', '9999-12-31', 'Y'),
    (143, 5, 50, '2016-01-01', '9999-12-31', 'Y'),
    (144, 5, 50, '2016-01-01', '9999-12-31', 'Y'),
    (145, 5, 50, '2016-01-01', '9999-12-31', 'Y'),
    (146, 5, 50, '2016-01-01', '9999-12-31', 'Y'),
    (147, 5, 50, '2016-01-01', '9999-12-31', 'Y'),
    (148, 5, 50, '2016-01-01', '9999-12-31', 'Y'),
    (149, 5, 50, '2016-01-01', '9999-12-31', 'Y'),
    (150, 5, 50, '2016-01-01', '9999-12-31', 'Y')
;
-- GO

/***************************************
Task 1  analytic functions
    
    Monthly stats for top 5 employees who resolved the most tickets per department for the latest 6 months
    Output: Month, Employee name, Department Name, # Tickets
***************************************/
WITH stats_base AS (
    SELECT
        FORMAT(t.closed_timestamp, 'yyyy-MM') AS closed_month,
        t.resolved_by_emp_id AS emp_id,
        e.dep_id,
        COUNT(ticket_id) AS tickets_closed
    FROM
        tickets AS t
    INNER JOIN
        employee_history AS e
    ON
        t.resolved_by_emp_id = e.emp_id
        AND CAST(t.closed_timestamp AS DATE) BETWEEN e.row_eff_date_start 
           AND e.row_eff_date_end
    GROUP BY
        FORMAT(t.closed_timestamp, 'yyyy-MM'),
        t.resolved_by_emp_id,
        e.dep_id
),
top_stats AS (
    SELECT
        closed_month,
        emp_id,
        dep_id,
        tickets_closed,
        SUM(tickets_closed) OVER (PARTITION BY closed_month, dep_id) AS total_dep_tickets_closed,
        RANK() OVER (PARTITION BY closed_month, dep_id ORDER BY tickets_closed DESC) AS rnk
    FROM
        stats_base
),
top_stats_ext AS (
    SELECT
        closed_month,
        emp_id,
        dep_id,
        tickets_closed,
        total_dep_tickets_closed,
        CAST(ROUND(100.00 * tickets_closed / total_dep_tickets_closed, 2) AS DECIMAL(10,2)) AS monthly_closed_percent,
        rnk,
        CAST(rnk AS VARCHAR(10)) AS rank_str,
        CAST(
            (LAG(rnk) OVER (PARTITION BY dep_id, emp_id ORDER BY closed_month) - rnk)
            AS VARCHAR(10)
        ) AS rank_change_str
    FROM
        top_stats
)
SELECT
    t.closed_month AS month,
    d.name AS dep_name,
    e.name AS emp_name,
    t.rank_str + ' (' + COALESCE(t.rank_change_str, 'N/A') + ')' AS month_rank,
    t.tickets_closed,
    t.total_dep_tickets_closed,
    t.monthly_closed_percent
FROM
    top_stats_ext AS t
INNER JOIN
    employees AS e
ON
    t.emp_id = e.emp_id
INNER JOIN
    departments AS d
ON
    t.dep_id = d.dep_id
WHERE
    t.closed_month >= FORMAT(DATEADD(month, -6, CURRENT_TIMESTAMP), 'yyyy-MM')
    AND rnk <= 5
    -- AND d.name IN ('D1', 'D2')
ORDER BY
    closed_month DESC,
    dep_name,
    month_rank
;
